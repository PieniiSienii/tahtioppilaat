'use strict';

// Define all functions first
function deleteReference(type, id) {
    if (confirm('Are you sure you want to delete this reference?')) {
        fetch(`/delete_reference/${type}/${id}`, {
            method: 'POST',
        }).then(() => {
            window.location.reload();
        });
    }
}

function editReference(type, id) {
    // Clear the form first
    document.querySelector('#referenceForm').reset();
    
    // Find and open the correct details section based on type
    let detailsSection;
    if (type === 'doi') {
        detailsSection = document.querySelector('details summary[name="add_by_doi"]').parentElement;
    } else if (type === 'article') {
        detailsSection = document.querySelector('details summary[name="add_article"]').parentElement;
    } else if (type === 'book') {
        detailsSection = document.querySelector('details summary[name="add_book"]').parentElement;
    } else if (type === 'inproceeding') {
        detailsSection = document.querySelector('details summary[name="add_conference_paper"]').parentElement;
    }
    
    if (detailsSection) {
        // Close all other sections
        document.querySelectorAll('details').forEach(d => d.removeAttribute('open'));
        // Open the correct section
        detailsSection.setAttribute('open', '');
    }
    
    // Populate the form with existing data
    const reference = document.querySelector(`#reference-${type}-${id}`);
    if (reference) {
        if (type === 'doi') {
            document.querySelector('#doi').value = reference.dataset.doi;
        } else if (type === 'article') {
            document.querySelector('#article_author').value = reference.dataset.author;
            document.querySelector('#article_title').value = reference.dataset.title;
            document.querySelector('#article_journal').value = reference.dataset.journal;
            document.querySelector('#article_year').value = reference.dataset.year;
        } else if (type === 'book') {
            document.querySelector('#book_author').value = reference.dataset.author;
            document.querySelector('#book_title').value = reference.dataset.title;
            document.querySelector('#book_book_title').value = reference.dataset.bookTitle;
            document.querySelector('#book_publisher').value = reference.dataset.publisher;
            document.querySelector('#book_year').value = reference.dataset.year;
        } else if (type === 'inproceeding') {
            document.querySelector('#inproceeding_author').value = reference.dataset.author;
            document.querySelector('#inproceeding_title').value = reference.dataset.title;
            document.querySelector('#inproceeding_book_title').value = reference.dataset.bookTitle;
            document.querySelector('#inproceeding_year').value = reference.dataset.year;
        }
    }
    
    // Change form action to edit instead of create
    const form = document.querySelector('#referenceForm');
    form.action = `/edit_reference/${type}/${id}`;
}

function viewBibTeX(type, id) {
    const bibtexDisplay = document.getElementById('bibtexDisplay');
    const currentButton = event.target; // Get the button that was clicked
    
    // If display is already visible and we're clicking the same reference, hide it
    if (bibtexDisplay.style.display === 'block' && 
        bibtexDisplay.dataset.currentRef === `${type}-${id}`) {
        bibtexDisplay.style.display = 'none';
        currentButton.style.backgroundColor = '#2196F3'; // Reset button color
        return;
    }

    // Show the display and mark this as the current reference
    bibtexDisplay.style.display = 'block';
    bibtexDisplay.dataset.currentRef = `${type}-${id}`;
    
    // Reset all BibTeX buttons to default color
    document.querySelectorAll('button[onclick^="viewBibTeX"]').forEach(btn => {
        btn.style.backgroundColor = '#2196F3';
    });
    
    // Highlight the current button
    currentButton.style.backgroundColor = '#1565C0'; // Darker blue for active state

    // Fetch BibTeX content from server
    fetch(`/view_bibtex/${type}/${id}`)
        .then(response => response.text())
        .then(bibtex => {
            document.getElementById('bibtexContent').textContent = bibtex;
        })
        .catch(error => {
            console.error('Error fetching BibTeX:', error);
            document.getElementById('bibtexContent').textContent = 'Error loading BibTeX entry';
        });
}

function copyBibTeX() {
    const bibtexContent = document.getElementById('bibtexContent').textContent;
    
    // Copy to clipboard
    navigator.clipboard.writeText(bibtexContent)
        .then(() => {
            const button = document.querySelector('#bibtexDisplay button');
            const originalText = button.innerHTML;
            
            // Show feedback
            button.innerHTML = 'Copied!';
            button.style.backgroundColor = '#4CAF50';
            
            // Reset button after 2 seconds
            setTimeout(() => {
                button.innerHTML = originalText;
                button.style.backgroundColor = '#2196F3';
            }, 2000);
        })
        .catch(err => {
            console.error('Failed to copy text: ', err);
            alert('Failed to copy to clipboard');
        });
}

async function exportAllBibTeX() {
    try {
        // Fetch BibTeX content from your export route
        const response = await fetch('/export_all_bibtex');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const bibtexContent = await response.text();
        
        // Create and trigger download
        const blob = new Blob([bibtexContent], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'references.bib';
        
        // Append link, trigger download, and cleanup
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        window.URL.revokeObjectURL(url);
    } catch (error) {
        console.error('Error exporting BibTeX:', error);
        alert('Failed to export BibTeX file. Please try again.');
    }
}



// Make functions globally available
window.deleteReference = deleteReference;
window.editReference = editReference;
window.viewBibTeX = viewBibTeX;
window.copyBibTeX = copyBibTeX;

// DOM Content Loaded event listener
document.addEventListener('DOMContentLoaded', function() {
    const detailsElements = document.querySelectorAll('details');
    const form = document.querySelector('#referenceForm');
    
    detailsElements.forEach(details => {
        details.addEventListener('click', (e) => {
            if (e.target.tagName === 'SUMMARY') {
                // Reset form when closing a section
                if (!details.hasAttribute('open')) {
                    form.reset();
                }
                
                // Close other sections and reset form when opening a new section
                detailsElements.forEach(otherDetails => {
                    if (otherDetails !== details) {
                        otherDetails.removeAttribute('open');
                        form.reset();
                    }
                });
            }
        });
    });

    // Also reset form when any details section is closed directly
    detailsElements.forEach(details => {
        details.addEventListener('toggle', (e) => {
            if (!details.hasAttribute('open')) {
                form.reset();
            }
        });
    });
});