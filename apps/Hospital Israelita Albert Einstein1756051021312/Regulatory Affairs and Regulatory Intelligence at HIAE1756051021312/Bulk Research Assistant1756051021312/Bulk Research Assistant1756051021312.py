import os
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from tapestrysdk import fetch_group_list, fetch_group_document, generate_report
import time
import json

# Create load_research_tasks directory if it doesn't exist
os.makedirs('load_research_tasks', exist_ok=True)

# Tapestry_id
tapestry_ids = 8

def fetch_groups(tapestry_id):
    """
    Fetches all available document groups from Tapestry.
    
    Args:
        tapestry_id (str): The Tapestry project API key
        
    Returns:
        list: List of group objects with 'id' and 'name' properties
    """
    try:
        response = fetch_group_list(tapestry_id)
        if response.get("success") and "body" in response:
            return response["body"]
        else:
            return []
    except Exception:
        return []
    
def fetch_documents(group_id):
    """
    Fetches all documents within a specific group.
    
    Args:
        group_id (str): The ID of the group to fetch documents from
        
    Returns:
        list: List of document objects with 'id' and 'name' properties
    """
    try:
        tapestry_id = tapestry_ids
        response = fetch_group_document(tapestry_id, group_id)
        if response.get("success") and "body" in response:
            return response["body"]
        else:
            return []
    except Exception:
        return []

def main():
    """
    Main application function that sets up the UI and handles all interactions.
    Creates a web interface with document selection, prompt editing, and analysis capabilities.
    """
    
    # Cache groups and documents to avoid repeated API calls
    groups_cache = {}
    documents_cache = {}

    # Default prompt that users can customize
    current_prompt = {"text": """ """}

    # Fetch all available groups from Tapestry and cache them
    groups = fetch_groups(tapestry_ids)
    if not groups:
        groups = []
    for g in groups:
        groups_cache[g["id"]] = g

    # Apple-style modern UI with clean, professional appearance
    styles = """
    <style>
    /* Apple-style color palette for modern, professional appearance */
    :root {
        --apple-blue: #007AFF;
        --apple-gray: #8E8E93;
        --apple-light-gray: #F2F2F7;
        --apple-dark-gray: #1C1C1E;
        --apple-white: #FFFFFF;
        --apple-black: #000000;
        --apple-green: #34C759;
        --apple-red: #FF3B30;
        --apple-orange: #FF9500;
        --apple-purple: #AF52DE;
        --apple-pink: #FF2D92;
        --apple-yellow: #FFCC02;
        --apple-indigo: #5856D6;
        --apple-teal: #5AC8FA;
        --apple-brown: #A2845E;
        --apple-mint: #00C7BE;
        --apple-cyan: #32ADE6;
    }
    
    /* Main application background */
    #rendered_cells {
        background-color: var(--apple-white) !important;
    }
    
    /* Main content area layout */
    .main_content {
        display: flex;
        flex-direction: column;
        gap: 4px;  /* Reduced from 16px to minimize spacing */
        padding: 60px 20px 20px 20px;  /* Increased top padding by 2x (30px -> 60px) */
    }
    
    /* Section containers for organized layout */
    .section-box {
        display: flex;
        flex-direction: column;
        gap: 0px;  /* No gap between sections to minimize spacing */
    }
    
    /* Horizontal section styling */
    .section-box.horizontal {
        flex-direction: row;
        align-items: center;
        gap: 20px;
    }
    
    /* Center alignment for document selection card */
    .choose_doc_card__wrapper {
        display: flex;
        justify-content: center;
    }
    
    /* Main document selection card styling */
    .choose_card {
        display: flex;
        flex-direction: column;
        gap: 100px;  /* 100px gap between sections */
        background-color: var(--apple-white);
        border-radius: 12px;
        width: 100%;
        padding: 0px;  /* Remove all padding */
        box-shadow: none;
        border: none;
    }
    
    /* Group dropdown styling */
    .groupDropdown select {
        border-radius: 8px;
        cursor: pointer;
        border: none;        /* Remove border */
        background-color: var(--apple-light-gray); /* Light grey fill */
        padding: 12px 18px;  /* Increased padding by 1.5x */
        font-size: 24px;     /* Increased font size by 1.5x */
        color: var(--apple-dark-gray) !important; /* Force text color */
    }
    
    /* Ensure dropdown text is visible */
    .groupDropdown select option {
        color: var(--apple-dark-gray) !important;
        background-color: var(--apple-white);
    }
    
    /* Fix dropdown display - target the actual dropdown widget */
    .groupDropdown .widget-dropdown {
        color: var(--apple-dark-gray) !important;
    }
    
    /* Target the dropdown button text specifically */
    .groupDropdown button {
        color: var(--apple-dark-gray) !important;
        background-color: var(--apple-light-gray) !important;
    }
    
    /* Ensure the selected value text is visible */
    .groupDropdown .widget-dropdown .widget-label {
        color: var(--apple-dark-gray) !important;
    }
    
    /* Document selection container */
    .documents_container {
        position: relative;
        background-color: var(--apple-white);
        border-radius: 12px;
        height: auto;        /* Auto height instead of fixed 400px */
        max-width: 1050px;   /* Increased max-width by 1.5x */
        padding: 8px;        /* Reduced padding */
        border: none;        /* Remove container border */
        overflow-y: visible; /* No scrolling needed */
        overflow-x: hidden;  /* Hide horizontal scroll */
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: flex-start;  /* Align to left */
        align-items: flex-start;      /* Align to top */
        gap: 8px;  /* Space between items */
    }
    
    /* Individual document checkbox styling */
    .documents_container div {
        background-color: var(--apple-white);
        padding: 16px 24px;  /* Increased padding by 2x */
        margin: 0;           /* Remove margin */
        border-radius: 0;    /* Remove border radius */
        display: flex;
        align-items: center;  /* Center vertically */
        justify-content: flex-start; /* Left align content */
        border: none;         /* Remove border */
        transition: none;     /* Remove hover effect */
        width: calc(25% - 6px); /* 4 items per row with gap consideration */
        min-width: 200px;    /* Minimum width */
        max-width: 250px;    /* Maximum width */
        box-sizing: border-box;
    }
    
    /* Select All checkbox styling */
    .select-all-checkbox {
        margin-bottom: 8px;  /* Reduced space below select all */
        padding: 16px 24px;  /* Increased padding by 2x */
        background-color: var(--apple-white);
        border-radius: 0;    /* Remove border radius */
        border: none;         /* Remove border */
        width: 100%;         /* Full width for select all */
        box-sizing: border-box;
    }
    
    .select-all-checkbox label {
        font-weight: 500;
        color: var(--apple-dark-gray);
        font-size: 16px;
    }
    
    /* Document checkbox labels */
    .documents_container label {
        font-size: 18px;     /* Reduced font size for better readability */
        color: var(--apple-dark-gray);
        cursor: pointer;
        font-weight: 500;
        line-height: 1.4;
        word-wrap: break-word;
        max-width: 100%;
    }
    
    /* Checkbox styling */
    .documents_container .widget-checkbox input[type="checkbox"] {
        margin-right: 16px;  /* Reduced margin */
        transform: scale(1.3); /* Reduced scale for better proportion */
        margin-top: 2px;     /* Align with text */
        border: 1px solid var(--apple-dark-gray); /* Ensure border is visible */
    }
    
    /* Analysis button styling */
    .analyse_button {
        border-radius: 8px;
        padding: 18px 36px;  /* Increased padding by 1.5x */
        background-color: var(--apple-green);  /* Changed to green */
        color: var(--apple-white);
        font-weight: 600;
        font-size: 24px;     /* Increased font size by 1.5x */
        border: none;
        cursor: pointer;
        transition: background-color 0.2s ease;
        text-align: center;  /* Center text horizontally */
        display: flex;
        align-items: center;
        justify-content: center;  /* Center content horizontally */
    }
    
    /* Button hover effect */
    .analyse_button:hover {
        background-color: #28A745;  /* Darker green on hover */
    }
    
    /* Navigation bar styling */
    .navbar {
        display: flex;
        justify-content: flex-start;
        padding: 16px 20px;
        background-color: var(--apple-white);
    }
    
    /* Navigation button styling */
    .navbar button {
        display: flex;
        align-items: center;
        justify-content: center;
        background: var(--apple-blue);
        color: var(--apple-white);
        padding: 12px 20px;
        margin-right: 12px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        font-weight: 500;
        font-size: 16px;
        transition: background-color 0.2s ease;
    }
    
    /* Navigation button hover effect */
    .navbar button:hover {
        background: #0056CC;
    }
    
    /* Prompt page styling */
    .prompt_page {
        width: auto;
        display: flex;
        flex-direction: column;
        gap: 4px;  /* Reduced from 16px */
        background-color: var(--apple-white);
        border-radius: 12px;
        padding: 16px;  /* Reduced from 24px */
        box-shadow: none;
        border: none;
    }
    
    /* Accordion styling */
    .accordion-header {
        background-color: var(--apple-white); /* White background */
        border: none;
        border-radius: 8px;
        padding: 0;  /* No padding */
        cursor: pointer;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        font-size: 24px;  /* Increased font size by 1.5x */
        font-weight: 600;
        color: var(--apple-dark-gray);
        transition: background-color 0.2s ease;
    }
    
    .accordion-header:hover {
        background-color: #E5E5EA; /* Slightly darker on hover */
    }
    
    .accordion-content {
        max-height: 35px; /* Increased from 20px to 35px to prevent squashing */
        overflow: hidden;
        transition: max-height 0.3s ease;
        background-color: var(--apple-light-gray);
        border-radius: 0 0 8px 8px;
        margin-top: 0;
        padding: 16px;
    }
    
    .accordion-content.expanded {
        max-height: 500px; /* Adjust based on content */
        margin-top: 8px;
    }
    
    /* Save/Load controls styling */
    .save-load-controls {
        display: flex;
        align-items: center;
        gap: 4px;  /* Reduced gap to 4px */
        margin-bottom: 8px;
        padding: 8px 0;
    }
    
    /* Status container styling */
    .status-container {
        display: flex;
        align-items: center;
        gap: 4px;
        margin-bottom: 16px;
        padding: 0;
    }
    
    /* Save dropdown styling */
    .save-dropdown select {
        border-radius: 8px;
        cursor: pointer;
        border: 1px solid var(--apple-light-gray);
        background-color: var(--apple-white);
        padding: 4px 12px; /* Reduced vertical padding from 8px to 4px (50% reduction) */
        font-size: 14px;
        color: var(--apple-dark-gray);
    }
    
    /* Load dropdown styling */
    .load-dropdown select {
        border-radius: 8px;
        cursor: pointer;
        border: 1px solid var(--apple-light-gray);
        background-color: var(--apple-white);
        padding: 4px 12px; /* Reduced vertical padding from 8px to 4px (50% reduction) */
        font-size: 14px;
        color: var(--apple-dark-gray);
    }
    
    /* Prompt input styling */
    .prompt_input, .prompt_input textarea {
        width: auto;
        border-radius: 8px;
        border: none;  /* Remove border */
        font-size: 16px;
        background-color: var(--apple-light-gray);  /* Light grey background */
    }
    
    /* Prompt textarea specific styling */
    .prompt_input textarea {
        padding: 0px;
        width: auto;
        height: 350px;
        resize: vertical;
        text-align: left;
    }
    
    /* Task name input styling */
    .task-name-input input {
        background-color: var(--apple-white) !important;
        border: 1px solid var(--apple-light-gray) !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
        font-size: 14px !important;
        color: var(--apple-dark-gray) !important;
        width: 200px !important;
        height: 35px !important;
        z-index: 1000 !important;
    }
    
    /* Task name container styling */
    .task-name-container {
        display: flex !important;
        align-items: center !important;
        margin: 4px 0px !important;
        z-index: 1000 !important;
    }

    /* Full screen loading overlay */
    .fullscreen-loader {
        position: fixed;  /* cover whole screen */
        top: 0;
        left: 0;
        inset: 0;
        width: 100%;
        height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(255,255,255,0.8);
        backdrop-filter: blur(8px); /* blur background */
        z-index: 2000;
    }

    /* Loading spinner animation */
    .fullscreen-loader .spinner {
        border: 4px solid var(--apple-light-gray);
        border-top: 4px solid var(--apple-blue);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        animation: spin 1s linear infinite;
    }

    /* Spinner rotation animation */
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }

    /* Result document row styling */
    .result_doc_row {
        display: flex;
        align-items: center;
        padding: 12px 16px;
        border-radius: 8px;
        background-color: var(--apple-light-gray);
        transition: background-color 0.2s ease;
        cursor: pointer;
        width: 100%;  /* Full width */
        max-width: 600px;  /* Increased max width */
        word-wrap: break-word;
        white-space: normal;
    }
    
    /* Result row hover effect */
    .result_doc_row:hover {
        background-color: #E5E5EA;
    }
    
    /* Results container styling */
    .results_box {
        margin-top: 16px;
        border-radius: 12px;
        background-color: var(--apple-white);
        padding: 20px;
        box-shadow: none;
        border: none;
    }
    
    /* Download button styling */
    .download_btn {
        background-color: var(--apple-blue);
        color: var(--apple-white);
        padding: 8px 16px;
        border-radius: 8px;
        font-weight: 600;
        font-size: 14px;
    }
    
    /* Download button hover effect */
    .download_btn:hover {
        background-color: #0056CC;
    }
    
    /* Result wrapper styling */
    .result_wrapper {
        padding: 16px;
        display: flex;
        flex-direction: column;
        gap: 12px;
        align-items: flex-start;  /* Left align all items */
    }
    
    /* Change prompt button styling */
    .change_prompt_button {
        border-radius: 8px;
        background-color: var(--apple-blue);
        color: var(--apple-white);
        font-weight: 600;
        font-size: 16px;
        padding: 12px 24px;
        border: none;
        cursor: pointer;
    }
    
    /* Change prompt button hover effect */
    .change_prompt_button:hover {
        background-color: #0056CC;
    }
    
    /* Application header styling */
    .app-header {
        position: relative;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding: 16px 24px;
        background-color: var(--apple-white);
    }
    
    /* Header content layout */
    .header-content {
        display: flex;
        align-items: center;
    }
    
    /* Logo container positioning */
    .header-logo-container {
        position: fixed;
        top: 24px;
        right: 36px;
        display: flex;
        align-items: center;
        z-index: 1000;
    }
    
    /* Logo image styling */
    .header-logo {
        height: 91px;  /* Increased by 30% from 70px */
        width: auto;
        border-radius: 8px;
    }
    
    /* Header title styling */
    .header-title {
        margin: 0;
        color: var(--apple-dark-gray);
        font-size: 31.2px;  /* Increased by 30% from 24px */
        font-weight: 600;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
    
    /* Typography improvements for all headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: var(--apple-dark-gray);
        font-size: 1.5em;  /* Increase heading size by 1.5x */
    }
    
    /* Body text styling */
    body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        color: var(--apple-dark-gray);
    }
    
    /* Toggle switch styling */
    .toggle-switch {
        position: relative;
        display: inline-block;
        width: 44.6px;  /* Reduced by 15% from 52.5px */
        height: 25px;   /* Reduced by 15% from 29.4px */
    }
    
    .toggle-switch input {
        opacity: 0;
        width: 0;
        height: 0;
    }
    
    .toggle-slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc;
        transition: .4s;
        border-radius: 25px;  /* Reduced by 15% from 29.4px */
    }
    
    .toggle-slider:before {
        position: absolute;
        content: "";
        height: 19.6px; /* Reduced by 15% from 23.1px */
        width: 19.6px;  /* Reduced by 15% from 23.1px */
        left: 2.7px;    /* Reduced by 15% from 3.15px */
        bottom: 2.7px;  /* Reduced by 15% from 3.15px */
        background-color: white;
        transition: .4s;
        border-radius: 50%;
    }
    
    input:checked + .toggle-slider {
        background-color: var(--apple-blue);
    }
    
    input:checked + .toggle-slider:before {
        transform: translateX(19.6px);  /* Reduced by 15% from 23.1px */
    }
    </style>
    """
    display(HTML(styles))

    # Full-screen overlay with spinner for long-running operations
    fullscreen_loader = widgets.HTML(
        """<div id="widget-loader" class="fullscreen-loader"><div class="spinner"></div></div>"""
    )
    fullscreen_loader.layout.display = "none"

    # Header with logo and application title
    header_html = widgets.HTML(
        '''<div class="app-header">
            <div class="header-content">
            </div>
            <div class="header-logo-container">
                <h1 class="header-title" style="margin-right: 20px;">Tapestry Research Assistant</h1>
                <img src="barkleyGPT copy.png" alt="Barkley Logo" class="header-logo">
            </div>
        </div>'''
    )
    
    # Empty navbar (previously had tab buttons, now removed for single-page design)
    navbar = widgets.HBox([])  # Empty navbar
    navbar.add_class("navbar")

    # Container for document checkboxes - dynamically populated based on group selection
    documents_container = widgets.VBox([])
    documents_container.add_class("documents_container")
    
    # Dropdown to select which group of documents to analyze
    dropdown_options = [(g["name"], g["id"]) for g in groups] or [("No groups available", None)]
    group_dropdown = widgets.Dropdown(
        options=dropdown_options,
        value=dropdown_options[0][1] if dropdown_options else None,  # Set first option ID as default
        description="",  # Remove description
        layout=widgets.Layout(width="330px")  # Increased by 10% from 300px
    )
    group_dropdown.add_class("groupDropdown")

    # Hidden checkbox to track toggle state
    toggle_checkbox = widgets.Checkbox(value=False, description="", indent=False)
    toggle_checkbox.layout.display = "none"  # Hide the actual checkbox
    
    # Toggle switch for knowledge base research
    toggle_html = widgets.HTML(
        f'''<div style="display: flex; align-items: center; gap: 18px;">
            <label class="toggle-switch">
                <input type="checkbox" id="knowledge-toggle" {"checked" if toggle_checkbox.value else ""}>
                <span class="toggle-slider"></span>
            </label>
            <span style="font-weight: 600; color: var(--apple-dark-gray); font-size: 1.5em; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">Full knowledge base access</span>
        </div>'''
    )

    # UI section for group selection with title, dropdown, and toggle
    choose_group_section = widgets.HBox([
        widgets.HTML("<h3 style='margin: 0; margin-right: 20px; display: inline-block;'>Which topic are we focusing on?</h3>"),
        group_dropdown,
        widgets.HTML("<div style='margin-left: 40px; display: flex; align-items: center; gap: 18px;'>"),
        toggle_html,
        widgets.HTML("</div>"),
    ])
    choose_group_section.add_class("section-box horizontal")

    # UI section for document selection with checkbox container
    choose_documents_section = widgets.VBox([
        documents_container,
    ])
    choose_documents_section.add_class("section-box")

    # Wrapper for group and document selection sections
    choose_doc_card = widgets.VBox([
        choose_group_section,
        choose_documents_section
    ])
    choose_doc_card.add_class("choose_doc_card")
    choose_doc_card__wrapper = widgets.VBox([choose_doc_card])
    choose_doc_card__wrapper.add_class("choose_doc_card__wrapper")

    # Toggle is now part of the topic selection section, so this section is empty
    choose_param_section = widgets.VBox([toggle_checkbox])

    # Save/Load functionality for research tasks
    def save_research_task(change):
        """Save current text input as a research task file."""
        if change["name"] == "value" and change["new"]:
            if change["new"] == "Save":
                # Do nothing for default "Save" option
                save_dropdown.value = "Save"
                return
            elif change["new"] == "+ Create New":
                # Show modal for new file name
                show_save_modal()
            else:
                # Overwrite existing file
                try:
                    file_path = os.path.join('load_research_tasks', change["new"])
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(text_input.value)
                    save_status.value = f"✅ Saved: {change['new']}"
                    # Reset dropdown
                    save_dropdown.value = "Save"
                except Exception as e:
                    save_status.value = f"❌ Error saving: {str(e)}"
    
    # Create task name input widget (initially hidden)
    task_name_input = widgets.Text(
        value="",
        placeholder="Enter task name and press Enter...",
        layout=widgets.Layout(width="200px", height="35px", display="none", margin="4px 0px")
    )
    task_name_input.add_class("task-name-input")
    
    def on_task_name_change(change):
        if change["name"] == "value" and change["new"].strip():
            task_name = change["new"].strip()
            save_new_task(task_name)
            # Clear input and hide it
            task_name_input.value = ""
            task_name_container.layout.display = "none"
            save_status.value = ""
            # Reset dropdown
            save_dropdown.value = "Save"
    
    task_name_input.observe(on_task_name_change, names="value")
    
    def show_save_modal():
        """Show modal for entering new file name."""
        # Show the input container and status
        task_name_container.layout.display = "flex"
        save_status.value = "Enter task name:"
    
    def save_new_task(task_name):
        """Save new task with given name."""
        try:
            file_path = os.path.join('load_research_tasks', f"{task_name}.txt")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text_input.value)
            save_status.value = f"✅ Saved: {task_name}.txt"
            # Refresh dropdowns
            refresh_load_dropdown()
            refresh_save_dropdown()
            # Reset dropdown
            save_dropdown.value = "Save"
        except Exception as e:
            save_status.value = f"❌ Error saving: {str(e)}"
    
    def load_research_task(change):
        """Load selected research task file into text input."""
        if change["name"] == "value" and change["new"]:
            if change["new"] == "Load":
                # Do nothing for default "Load" option
                load_dropdown.value = "Load"
                return
            elif change["new"] != "Select task":
                try:
                    file_path = os.path.join('load_research_tasks', change["new"])
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    text_input.value = content
                    load_status.value = f"✅ Loaded: {change['new']}"
                except Exception as e:
                    load_status.value = f"❌ Error loading: {str(e)}"
    
    def refresh_load_dropdown():
        """Refresh the load dropdown with available files."""
        try:
            files = [f for f in os.listdir('load_research_tasks') if f.endswith('.txt')]
            options = [("Load", "Load"), ("Select task", "Select task")]
            if files:
                options.extend([(f, f) for f in sorted(files)])
            load_dropdown.options = options
        except Exception as e:
            load_dropdown.options = [("Load", "Load"), ("Select task", "Select task")]
    
    def refresh_save_dropdown():
        """Refresh the save dropdown with available files."""
        try:
            files = [f for f in os.listdir('load_research_tasks') if f.endswith('.txt')]
            options = [("Save", "Save"), ("+ Create New", "+ Create New")]
            if files:
                options.extend([(f, f) for f in sorted(files)])
            save_dropdown.options = options
        except Exception as e:
            save_dropdown.options = [("Save", "Save"), ("+ Create New", "+ Create New")]
    
    # Create save/load UI elements with proper default values
    save_dropdown = widgets.Dropdown(
        options=[("Save", "Save"), ("+ Create New", "+ Create New")],
        value="Save",  # Set default value to "Save"
        description="",
        layout=widgets.Layout(width="150px", height="35px")
    )
    save_dropdown.add_class("save-dropdown")
    save_dropdown.observe(save_research_task, names="value")
    
    save_status = widgets.HTML(value="", layout=widgets.Layout(width="200px"))
    
    load_dropdown = widgets.Dropdown(
        options=[("Load", "Load"), ("Select task", "Select task")],  # Add "Load" as first option
        value="Load",  # Set default value to "Load"
        description="",
        layout=widgets.Layout(width="200px", height="35px")
    )
    load_dropdown.add_class("load-dropdown")
    load_dropdown.observe(load_research_task, names="value")
    
    load_status = widgets.HTML(value="", layout=widgets.Layout(width="200px"))
    
    # Initial load of available files
    refresh_load_dropdown()
    refresh_save_dropdown()
    
    # Save/Load controls container
    save_load_controls = widgets.HBox([
        load_dropdown,
        widgets.HTML("<div style='width: 4px;'></div>"),  # Spacer
        save_dropdown
    ])
    save_load_controls.add_class("save-load-controls")
    
    # Task name input container (initially hidden)
    task_name_container = widgets.HBox([
        widgets.HTML("<div style='width: 154px;'></div>"),  # Spacer to align with save dropdown
        task_name_input
    ])
    task_name_container.layout.display = "none"
    task_name_container.add_class("task-name-container")
    
    # Status messages container (separate from controls)
    status_container = widgets.HBox([
        load_status,
        widgets.HTML("<div style='width: 4px;'></div>"),  # Spacer
        save_status
    ])
    status_container.add_class("status-container")

    # Large text area for users to enter custom analysis instructions
    text_input = widgets.Textarea(
        value=current_prompt["text"],
        description="Prompt:", 
        layout=widgets.Layout(height='350px')
    )
    text_input.style.description_width = "0px"
    text_input.add_class("prompt_input")

    # Create clickable button for accordion header
    accordion_button = widgets.Button(
        description="What research task would you like me to perform?",
        button_style="",
        layout=widgets.Layout(
            width="100%",
            height="auto",
            border="none",
            background_color="var(--apple-white)",
            color="var(--apple-dark-gray)",
            font_size="24px",
            font_weight="600",
            text_align="left",
            padding="0"
        )
    )
    accordion_button.add_class("accordion-header")
    
    # Create accordion content container
    accordion_content = widgets.VBox([save_load_controls, task_name_container, status_container, text_input])
    accordion_content.add_class("accordion-content")
    
    # Track accordion state
    accordion_expanded = True  # Start expanded so text input is visible
    
    # Accordion toggle function
    def toggle_accordion(b):
        nonlocal accordion_expanded
        accordion_expanded = not accordion_expanded
        
        if accordion_expanded:
            accordion_content.add_class("expanded")
            accordion_button.layout.background_color = "var(--apple-white)"
        else:
            accordion_content.remove_class("expanded")
            accordion_button.layout.background_color = "var(--apple-white)"
    
    # Attach click handler
    accordion_button.on_click(toggle_accordion)
    
    # Initially show content (expanded by default)
    accordion_content.add_class("expanded")
    accordion_button.layout.background_color = "var(--apple-white)"
    
    # Prompt section with accordion structure
    prompt_section = widgets.VBox([
        accordion_button,
        accordion_content
    ])
    prompt_section.add_class("section-box")

    # Button to start the document analysis process
    analyse_button = widgets.Button(
        description="Go!", 
        button_style="primary", 
        layout=widgets.Layout(width="120px")  # Reduced width to prevent text truncation
    )
    analyse_button.add_class("analyse_button")

    # Combines all sections into the main application card
    choose_card = widgets.VBox([
        prompt_section,
        choose_doc_card__wrapper,
        analyse_button
    ])
    choose_card.add_class("choose_card")
    
    # Container for displaying analysis results and download links
    results_box = widgets.VBox([])
    results_box.add_class("results_box")

    # Combines the main content and results into a single page
    main_page = widgets.VBox([
        choose_card, 
        results_box
    ], layout=widgets.Layout(padding="15px"))

    def show_loader():
        """Shows the full-screen loading overlay with spinner."""
        fullscreen_loader.layout.display = "flex"

    def hide_loader():
        """Hides the full-screen loading overlay."""
        fullscreen_loader.layout.display = "none"

    # Handles the dynamic loading of documents when a group is selected
    def on_group_change(change):
        """Handles group selection changes by loading documents for the selected group."""
        print(f"Dropdown change detected: {change}")  # Debug output
        if change["name"] == "value" and change["new"] is not None:
            group_id = change["new"]
            print(f"Loading documents for group: {group_id}")  # Debug output

            show_loader()
            try:
                # Fetch documents for the selected group
                docs = fetch_documents(group_id)
                documents_cache[group_id] = docs
                
                if docs:
                    # Create "Select All" checkbox
                    select_all_checkbox = widgets.Checkbox(
                        value=False,
                        description="Select All Documents",
                        indent=False
                    )
                    select_all_checkbox.add_class("select-all-checkbox")
                    
                    # Create checkboxes for each document with enhanced information
                    document_checkboxes = []
                    for d in docs:
                        # Get document name and try to extract additional info
                        doc_name = d.get("name", f"Document {d['id']}")
                        doc_id = d.get("id", "")
                        
                        # Create enhanced description with file info
                        description = f"{doc_name}"
                        if d.get("size"):
                            description += f" ({d['size']})"
                        if d.get("created_at"):
                            description += f" - Created: {d['created_at'][:10]}"  # Show just date
                        
                        checkbox = widgets.Checkbox(
                            value=False,
                            description=description,
                            indent=False
                        )
                        checkbox.add_class("document-checkbox")
                        document_checkboxes.append(checkbox)
                    
                    # Add select all functionality
                    def on_select_all_change(change):
                        for cb in document_checkboxes:
                            cb.value = change["new"]
                    
                    select_all_checkbox.observe(on_select_all_change, names="value")
                    
                    # Combine select all and document checkboxes
                    documents_container.children = [select_all_checkbox] + document_checkboxes
                else:
                    documents_container.children = []  # Empty container when no documents
            except Exception as e:
                documents_container.children = [widgets.Label(f"⚠️ Error: {e}")]
            finally:
                hide_loader()

    # Connect the group dropdown to the document loading handler
    group_dropdown.observe(on_group_change, names="value")
    
    # Prevent any default form submission behavior
    group_dropdown.layout.width = "330px"  # Ensure layout is set

    # Output widget for displaying the main application content
    main_content = widgets.Output()
    main_content.add_class("main_content")

    def show_main_page(_=None):
        """Displays the main application page in the content area."""
        with main_content:
            clear_output()
            display(main_page)

    # Core function that handles the document analysis process
    def on_analyse_click(b):
        """
        Handles the analysis button click event.
        
        This function:
        1. Collects selected document IDs
        2. Validates user selections
        3. Calls the Tapestry SDK for analysis
        4. Displays results with download links
        """
        # Clear previous results
        results_box.children = []

        # Collect IDs of all selected documents from checkboxes (skip the first "Select All" checkbox)
        selected_docs = [
            d["id"] for i, d in enumerate(documents_cache.get(group_dropdown.value, []))
            if isinstance(documents_container.children[i+1], widgets.Checkbox)  # +1 to skip "Select All"
            and documents_container.children[i+1].value
        ]
        
        # Validate that at least one document is selected
        if not selected_docs:
            results_box.children = [widgets.Label("⚠️ No documents selected!")]
            return
        
        # Prepare all parameters for the analysis request
        tapestry_id = tapestry_ids
        group_id = group_dropdown.value
        is_chat = toggle_checkbox.value  # Whether to research across knowledge base
        user_prompt = text_input.value  # Custom analysis instructions

        # Show loading indicator during analysis
        show_loader()
        try:
            # Call the Tapestry SDK to perform the analysis
            response = generate_report(
                tapestry_id=tapestry_id,
                group_id=group_id,
                document_ids=selected_docs,  # List of all selected document IDs
                is_chat=is_chat,            # Research across knowledge base if toggled
                user_prompt=user_prompt     # Custom analysis instructions
            )

            # Process and display the analysis results
            if response.get("success") and "body" in response:
                docs = response["body"]  # Dictionary of {title: download_url}
                
                # Create results header
                res_header = widgets.HTML("<h3 style='margin: 0; margin-bottom: 16px; text-align: left;'>Outputs</h3>")

                # Create clickable document links for each generated report
                rows = []
                for title, url in docs.items():
                    # Determine file type and icon
                    file_extension = title.lower().split('.')[-1] if '.' in title else 'doc'
                    if file_extension in ['doc', 'docx']:
                        icon = "📄"  # Document icon
                    elif file_extension == 'pdf':
                        icon = "📕"  # PDF icon
                    elif file_extension in ['txt', 'text']:
                        icon = "📝"  # Text icon
                    else:
                        icon = "📄"  # Default document icon
                    
                    # Create clickable document row
                    box = widgets.HTML(
                        f'<a href="{url}" target="_blank" download style="text-decoration:none;">'
                        f'<div class="result_doc_row">{icon} {title}</div>'
                        '</a>'
                    )
                    rows.append(box)
                
                # Combine header and download rows
                result_wrapper = widgets.VBox([
                    res_header,
                    *rows
                ])
                result_wrapper.add_class("result_wrapper")
                results_box.children = [result_wrapper]
            else:
                # Handle analysis failure
                results_box.children = [widgets.Label("⚠️ Analysis failed or empty response.")]
        except Exception as e:
            # Handle any errors during analysis
            results_box.children = [widgets.Label(f"⚠️ Error: {e}")]
        finally:
            # Always hide loading indicator when done
            hide_loader()

    # Connect the analysis button to the analysis handler
    analyse_button.on_click(on_analyse_click)

    # Combine all UI components into the final application layout
    app = widgets.VBox([header_html, navbar, main_content, fullscreen_loader])
    
    # Display the main page initially
    with main_content:
        show_main_page()
    display(app)

    # Load documents for the initially selected group (if any)
    if group_dropdown.value:
        on_group_change({"name": "value", "new": group_dropdown.value})

# Run the main application function to start the Document Research Assistant
main()