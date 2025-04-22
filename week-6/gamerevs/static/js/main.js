// Main JavaScript file for GameRevs

// Import helper functions from review-helper.js
import { formatReviewDate, truncateReview, calculateAverageRating, displayStarRating } from './review-helper.js';

document.addEventListener('DOMContentLoaded', function() {
    console.log('GameRevs application loaded');
    
    // Initialize any interactive elements
    initRatingSystem();
    initFormValidation();
    initReviewFeatures();
});

// Function to handle the star rating system
function initRatingSystem() {
    const ratingElements = document.querySelectorAll('.rating-select');
    
    ratingElements.forEach(element => {
        element.addEventListener('click', function(e) {
            if (e.target.classList.contains('star')) {
                const value = e.target.dataset.value;
                const stars = element.querySelectorAll('.star');
                
                // Update visual feedback
                stars.forEach(star => {
                    if (parseInt(star.dataset.value) <= parseInt(value)) {
                        star.classList.add('selected');
                    } else {
                        star.classList.remove('selected');
                    }
                });
                
                // Update hidden input value
                const input = element.querySelector('input[type="hidden"]');
                if (input) {
                    input.value = value;
                }
            }
        });
    });
}

// Function to validate form submissions
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            let isValid = true;
            const requiredFields = form.querySelectorAll('[required]');
            
            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    field.classList.add('error');
                    
                    // Add error message if not already present
                    let errorMsg = field.nextElementSibling;
                    if (!errorMsg || !errorMsg.classList.contains('error-message')) {
                        errorMsg = document.createElement('span');
                        errorMsg.classList.add('error-message');
                        errorMsg.textContent = 'This field is required.';
                        field.parentNode.insertBefore(errorMsg, field.nextSibling);
                    }
                } else {
                    field.classList.remove('error');
                    
                    // Remove error message if present
                    const errorMsg = field.nextElementSibling;
                    if (errorMsg && errorMsg.classList.contains('error-message')) {
                        errorMsg.remove();
                    }
                }
            });
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    });
}

// Function to initialize review features using the helper functions
function initReviewFeatures() {
    // Format all review dates
    const reviewDates = document.querySelectorAll('.review-date');
    reviewDates.forEach(dateElement => {
        const originalDate = dateElement.textContent || dateElement.dataset.date;
        if (originalDate) {
            dateElement.textContent = formatReviewDate(originalDate);
        }
    });
    
    // Truncate long review text
    truncateReview('.review-content', 200);
    
    // Display star ratings
    const reviewRatings = document.querySelectorAll('.review-rating');
    reviewRatings.forEach(ratingElement => {
        const ratingValue = ratingElement.dataset.rating;
        if (ratingValue) {
            displayStarRating(`#${ratingElement.id}`, ratingValue);
        }
    });
    
    // Calculate and display average ratings if needed
    const gameCards = document.querySelectorAll('.game-card');
    gameCards.forEach(card => {
        const ratingElements = card.querySelectorAll('.user-rating');
        if (ratingElements.length > 0) {
            const ratings = Array.from(ratingElements).map(el => 
                parseFloat(el.dataset.rating || el.textContent)
            );
            
            const avgRating = calculateAverageRating(ratings);
            const avgElement = card.querySelector('.average-rating');
            if (avgElement) {
                avgElement.textContent = avgRating;
                displayStarRating(`#${avgElement.id}-stars`, avgRating);
            }
        }
    });
    
    // Add sorting functionality for reviews
    initReviewSorting();
}

// Function to handle review sorting
function initReviewSorting() {
    const sortSelect = document.querySelector('#sort-reviews');
    if (!sortSelect) return;
    
    sortSelect.addEventListener('change', function() {
        const reviewContainer = document.querySelector('.reviews-container');
        const reviews = Array.from(reviewContainer.querySelectorAll('.review-item'));
        
        // Sort the reviews based on the selected option
        reviews.sort((a, b) => {
            const sortBy = sortSelect.value;
            
            if (sortBy === 'date-newest') {
                const dateA = new Date(a.querySelector('.review-date').dataset.date);
                const dateB = new Date(b.querySelector('.review-date').dataset.date);
                return dateB - dateA;
            } else if (sortBy === 'date-oldest') {
                const dateA = new Date(a.querySelector('.review-date').dataset.date);
                const dateB = new Date(b.querySelector('.review-date').dataset.date);
                return dateA - dateB;
            } else if (sortBy === 'rating-highest') {
                const ratingA = parseFloat(a.querySelector('.review-rating').dataset.rating);
                const ratingB = parseFloat(b.querySelector('.review-rating').dataset.rating);
                return ratingB - ratingA;
            } else if (sortBy === 'rating-lowest') {
                const ratingA = parseFloat(a.querySelector('.review-rating').dataset.rating);
                const ratingB = parseFloat(b.querySelector('.review-rating').dataset.rating);
                return ratingA - ratingB;
            }
            return 0;
        });
        
        // Reappend the sorted reviews
        reviews.forEach(review => {
            reviewContainer.appendChild(review);
        });
    });
} 