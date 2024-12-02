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
    // Show the BibTeX display column
    const bibtexDisplay = document.getElementById('bibtexDisplay');
    bibtexDisplay.style.display = 'block';

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

// Make functions globally available
window.deleteReference = deleteReference;
window.editReference = editReference;
window.viewBibTeX = viewBibTeX;

// DOM Content Loaded event listener
document.addEventListener('DOMContentLoaded', function() {
    const detailsElements = document.querySelectorAll('details');
    
    detailsElements.forEach(details => {
        details.addEventListener('click', (e) => {
            if (e.target.tagName === 'SUMMARY') {
                detailsElements.forEach(otherDetails => {
                    if (otherDetails !== details) {
                        otherDetails.removeAttribute('open');
                    }
                });
            }
        });
    });
});