/**
 * review-helper.js
 * Helper functions for the game review functionality
 */

// Function to format date in a user-friendly way
export function formatReviewDate(dateString) {
  const date = new Date(dateString);
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return date.toLocaleDateString(undefined, options);
}

// Function to truncate review text with "Read more" option
export function truncateReview(element, maxLength = 150) {
  const reviewElements = document.querySelectorAll(element);
  
  reviewElements.forEach(review => {
    const fullText = review.textContent;
    
    if (fullText.length <= maxLength) return;
    
    const truncated = fullText.substr(0, maxLength).trim() + '...';
    const fullTextHidden = document.createElement('span');
    fullTextHidden.classList.add('full-review-text');
    fullTextHidden.style.display = 'none';
    fullTextHidden.textContent = fullText;
    
    const truncatedElem = document.createElement('span');
    truncatedElem.classList.add('truncated-text');
    truncatedElem.textContent = truncated;
    
    const readMoreBtn = document.createElement('button');
    readMoreBtn.classList.add('read-more-btn');
    readMoreBtn.textContent = 'Read more';
    
    readMoreBtn.addEventListener('click', function() {
      if (fullTextHidden.style.display === 'none') {
        fullTextHidden.style.display = 'inline';
        truncatedElem.style.display = 'none';
        readMoreBtn.textContent = 'Read less';
      } else {
        fullTextHidden.style.display = 'none';
        truncatedElem.style.display = 'inline';
        readMoreBtn.textContent = 'Read more';
      }
    });
    
    // Clear the original content and append new elements
    review.textContent = '';
    review.appendChild(truncatedElem);
    review.appendChild(fullTextHidden);
    review.appendChild(readMoreBtn);
  });
}

// Function to calculate average rating
export function calculateAverageRating(ratings) {
  if (!ratings || ratings.length === 0) return 0;
  
  const sum = ratings.reduce((total, rating) => total + rating, 0);
  return (sum / ratings.length).toFixed(1);
}

// Function to display star ratings visually
export function displayStarRating(container, rating) {
  const starContainer = document.querySelector(container);
  if (!starContainer) return;
  
  starContainer.innerHTML = '';
  
  // Convert rating to number between 0 and 5
  const numericRating = parseFloat(rating);
  if (isNaN(numericRating)) return;
  
  const fullStars = Math.floor(numericRating);
  const hasHalfStar = numericRating - fullStars >= 0.5;
  
  // Add full stars
  for (let i = 0; i < fullStars; i++) {
    const star = document.createElement('span');
    star.innerHTML = '★';
    star.classList.add('star', 'full');
    starContainer.appendChild(star);
  }
  
  // Add half star if needed
  if (hasHalfStar) {
    const halfStar = document.createElement('span');
    halfStar.innerHTML = '★';
    halfStar.classList.add('star', 'half');
    starContainer.appendChild(halfStar);
  }
  
  // Add empty stars
  const emptyStars = 5 - fullStars - (hasHalfStar ? 1 : 0);
  for (let i = 0; i < emptyStars; i++) {
    const emptyStar = document.createElement('span');
    emptyStar.innerHTML = '☆';
    emptyStar.classList.add('star', 'empty');
    starContainer.appendChild(emptyStar);
  }
} 