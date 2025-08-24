# Document Research Assistant - Tapestry Bulk Analysis Tool

## Overview

This application provides a web interface for bulk analysis of documents stored in Tapestry. Users can select multiple documents and run AI-powered analysis with custom prompts to identify gaps, insights, and generate reports.

## Features

- **Document Selection**: Choose from multiple document groups and select individual documents for analysis
- **Custom Prompts**: Define custom analysis instructions to guide the AI analysis
- **Knowledge Base Research**: Toggle option to include broader knowledge base research in the analysis
- **Bulk Processing**: Analyze multiple documents simultaneously
- **Output Generation**: Download analysis outputs in various formats
- **Modern UI**: Clean, Apple-style interface with professional appearance

## Technical Architecture

### Core Components

#### 1. Data Fetching Functions
- **`fetch_groups(tapestry_id)`**: Retrieves all available document groups from Tapestry
- **`fetch_documents(group_id)`**: Fetches all documents within a specific group

#### 2. Main Application Function
- **`main()`**: Sets up the UI and handles all user interactions
- **Cache Management**: Stores groups and documents to avoid repeated API calls
- **Event Handling**: Manages user interactions and state changes

#### 3. User Interface Components

##### Header Section
- **Logo Positioning**: Barkley logo positioned in top-right corner
- **Application Title**: "Document Research Assistant" displayed prominently
- **Clean Design**: No borders or horizontal lines for modern appearance

##### Document Selection Interface
- **Group Dropdown**: Select which group of documents to analyze
- **Document Checkboxes**: Multi-select interface for choosing documents
- **Dynamic Loading**: Documents load automatically when group is selected

##### Analysis Configuration
- **Prompt Text Area**: Large text area for custom analysis instructions
- **Chat Integration**: Checkbox to include chat/conversation data
- **Analysis Button**: Triggers the document analysis process

##### Results Display
- **Output List**: Shows generated analysis outputs
- **Clickable Downloads**: Click any output to download directly
- **Error Handling**: Clear error messages for failed operations

#### 4. Analysis Process

##### Document Selection Validation
```python
selected_docs = [
    d["id"] for i, d in enumerate(documents_cache.get(group_dropdown.value, []))
    if isinstance(documents_container.children[i], widgets.Checkbox) 
    and documents_container.children[i].value
]
```

##### Parameter Preparation
- **Tapestry ID**: Project API key for authentication
- **Group ID**: Selected document group
- **Document IDs**: List of selected document IDs
- **Knowledge Base Flag**: Whether to research across the knowledge base
- **User Prompt**: Custom analysis instructions

##### SDK Integration
```python
response = generate_report(
    tapestry_id=tapestry_id,
    group_id=group_id,
    document_ids=selected_docs,  # List of all selected document IDs
    is_chat=is_chat,            # Research across knowledge base if toggled
    user_prompt=user_prompt     # Custom analysis instructions
)
```

### Styling System

#### Apple-Style Design
- **Color Palette**: Modern Apple-inspired colors using CSS variables
- **Typography**: System fonts for consistent appearance
- **Spacing**: Consistent padding and margins throughout
- **Interactive Elements**: Light grey backgrounds for input fields

#### Key CSS Classes
- **`.main_content`**: Main application layout
- **`.choose_card`**: Document selection container
- **`.documents_container`**: Document checkbox area
- **`.analyse_button`**: Primary action button
- **`.results_box`**: Results display area

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip package manager
- Tapestry project API key

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd tapestry_bulk_eval/
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API key**
   - Edit `Bulk_Research_Assistant1756051021312.py`
   - Replace `tapestry_ids = "xx-xxxxxxxxx-xxxxxxxx"` with your actual API key

5. **Add logo image**
   - Place `barkleyGPT copy.png` in the project directory (or use the embedded base64 version)

### Running the Application

1. **Navigate to the project directory**
   ```bash
   cd /Users/user/Desktop/Barkley/tapestry/src_tap/apps/int/int_ops/bulk_gap_analysis/tapestry_bulk_eval
   ```

2. **Activate virtual environment**
   ```bash
   source .venv/bin/activate
   ```

3. **Convert Python to Notebook**
   ```bash
   jupytext --to notebook Bulk_Research_Assistant1756051021312.py
   ```

4. **Start Voila server**
   ```bash
   voila Bulk_Research_Assistant1756051021312.ipynb --port=8866 --no-browser
   ```

5. **Access the application**
   - Open browser to `http://localhost:8866`
   - The application will load with the document selection interface
   - Open browser to `http://localhost:8866`
   - The application will load with the document selection interface

## Usage Guide

### Step 1: Select Document Group
1. Use the "Which Topic do you want me to focus on?" dropdown to choose a document group
2. Documents will automatically load and display as checkboxes

### Step 2: Choose Documents
1. Check the boxes next to documents you want to analyze
2. You can select multiple documents for bulk analysis

### Step 3: Configure Analysis
1. **Edit Prompt**: Enter custom instructions for the AI analysis
   - Examples:
     - "Analyze these documents for compliance gaps"
     - "Find security vulnerabilities mentioned in these documents"
     - "Summarize key findings and recommendations"
     - "Identify missing information or incomplete sections"

2. **Research across the knowledge base**: Toggle this option if you want to include broader knowledge base research in the analysis

### Step 4: Run Analysis
1. Click the "Run Analysis" button
2. A loading spinner will appear during processing
3. Results will display with download links for each report

### Step 5: Download Outputs
1. Click on any output document to download it
2. Outputs will download in the browser's default download location

## Technical Details

### Dependencies

#### Core Libraries
- **`ipywidgets`**: Interactive UI components
- **`IPython.display`**: Display and output management
- **`tapestrysdk`**: Tapestry API integration
- **`voila`**: Jupyter notebook to web application conversion

#### SDK Functions Used
- **`fetch_group_list()`**: Retrieve document groups
- **`fetch_group_document()`**: Get documents in a group
- **`generate_report()`**: Perform AI analysis and generate outputs

### Data Flow

1. **Initialization**
   - Load available groups from Tapestry
   - Cache group data for performance

2. **User Interaction**
   - User selects group → Load documents for that group
   - User selects documents → Validate selections
   - User enters prompt → Store custom instructions

3. **Analysis Execution**
   - Collect selected document IDs
   - Prepare analysis parameters
   - Call Tapestry SDK with all parameters
   - SDK handles document chunking and LLM processing internally

4. **Results Processing**
   - Receive analysis results from SDK
   - Display clickable outputs for download
   - Handle errors and provide user feedback

### Error Handling

- **No Documents Selected**: Clear error message
- **API Failures**: Exception handling with user-friendly messages
- **Empty Results**: Appropriate feedback for failed analysis
- **Network Issues**: Loading states and timeout handling

### Performance Optimizations

- **Caching**: Groups and documents cached to reduce API calls
- **Lazy Loading**: Documents only loaded when group is selected
- **Efficient UI Updates**: Minimal re-rendering of components

## Customization

### Styling Modifications
- Edit the CSS variables in the `styles` section
- Modify color palette by changing `:root` variables
- Adjust spacing and layout through CSS classes

### Functionality Extensions
- Add new analysis parameters
- Implement additional document filters
- Create custom result formats
- Add export functionality

### API Integration
- Extend with additional Tapestry SDK functions
- Implement custom analysis workflows
- Add support for different document types

## Troubleshooting

### Common Issues

1. **"No groups available"**
   - Check API key configuration
   - Verify Tapestry project access
   - Ensure network connectivity

2. **"No documents found"**
   - Selected group may be empty
   - Check document permissions
   - Verify group ID is valid

3. **Analysis fails**
   - Ensure at least one document is selected
   - Check prompt text is not empty
   - Verify API key has analysis permissions

4. **UI not loading**
   - Check Voila server is running
   - Verify port 8866 is available
   - Check browser console for errors

### Debug Mode
Run Voila with debug flags for detailed error information:
```bash
voila main.ipynb --port=8866 --no-browser --show_tracebacks=True --debug
```

## Development Notes

### Code Structure
- **Modular Design**: Functions separated by responsibility
- **Event-Driven**: UI updates based on user interactions
- **State Management**: Centralized state handling
- **Error Boundaries**: Comprehensive error handling

### Best Practices
- **Documentation**: Comprehensive docstrings and comments
- **Type Hints**: Consider adding type annotations
- **Testing**: Add unit tests for core functions
- **Logging**: Implement proper logging for debugging

### Future Enhancements
- **User Authentication**: Add login system
- **Report Templates**: Customizable report formats
- **Batch Processing**: Queue-based analysis for large datasets
- **Real-time Updates**: WebSocket integration for live progress
- **Export Options**: Multiple file format support
- **Analysis History**: Track and review previous analyses

## License

This project is proprietary software developed for internal use.

## Support

For technical support or feature requests, contact the development team.


