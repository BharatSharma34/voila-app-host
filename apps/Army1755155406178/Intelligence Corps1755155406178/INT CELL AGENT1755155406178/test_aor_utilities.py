#!/usr/bin/env python3
"""
Test script for AOR Cell utility functions.

This script demonstrates how to use the AOR Cell management utilities
that were added to the main application.
"""

import sys
import os

# Add the current directory to the path so we can import from the main file
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the utility functions from the main application
try:
    from Critical_Int_1754487352099 import (
        list_aor_cells, 
        delete_aor_cell, 
        clear_all_aor_cells,
        _refresh_workspace_dropdown
    )
except ImportError as e:
    print(f"Error importing functions: {e}")
    print("Make sure you're running this from the same directory as the main application file.")
    sys.exit(1)

def test_list_aor_cells():
    """Test listing all AOR Cells."""
    print("=== Listing All AOR Cells ===")
    cells = list_aor_cells()
    if cells:
        print(f"Found {len(cells)} AOR Cell(s):")
        for cell in cells:
            print(f"  - ID: {cell['workspace_id']}, Name: {cell['workspace_name']}")
    else:
        print("No AOR Cells found.")
    print()

def test_delete_specific_cell():
    """Test deleting a specific AOR Cell."""
    print("=== Testing AOR Cell Deletion ===")
    
    # First, list current cells
    cells = list_aor_cells()
    if not cells:
        print("No AOR Cells to delete.")
        return
    
    # Try to delete the first non-default cell
    for cell in cells:
        if cell['workspace_id'] != 'default':
            print(f"Attempting to delete AOR Cell: {cell['workspace_name']} (ID: {cell['workspace_id']})")
            success = delete_aor_cell(cell['workspace_id'])
            if success:
                print(f"✓ Successfully deleted AOR Cell: {cell['workspace_name']}")
            else:
                print(f"✗ Failed to delete AOR Cell: {cell['workspace_name']}")
            break
    else:
        print("No non-default AOR Cells found to delete.")
    print()

def test_clear_all_cells():
    """Test clearing all AOR Cells (except default)."""
    print("=== Testing Clear All AOR Cells ===")
    print("This will remove all AOR Cells except 'default'.")
    
    response = input("Do you want to proceed? (y/N): ").strip().lower()
    if response == 'y':
        success = clear_all_aor_cells()
        if success:
            print("✓ Successfully cleared all AOR Cells (except default)")
        else:
            print("✗ Failed to clear AOR Cells")
    else:
        print("Operation cancelled.")
    print()

def main():
    """Main test function."""
    print("AOR Cell Utility Functions Test")
    print("=" * 40)
    print()
    
    # Test 1: List all AOR Cells
    test_list_aor_cells()
    
    # Test 2: Delete a specific cell
    test_delete_specific_cell()
    
    # Test 3: Clear all cells (with confirmation)
    test_clear_all_cells()
    
    # Final list
    print("=== Final AOR Cell List ===")
    test_list_aor_cells()
    
    print("Test completed!")

if __name__ == "__main__":
    main() 