/**
 * toggle-details.js
 * Provides functionality for toggling the visibility of extended game details
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize toggle details functionality
  initToggleDetails();
});

/**
 * Sets up event listeners for toggling game details sections
 */
function initToggleDetails() {
  // Find all detail toggle buttons
  const detailButtons = document.querySelectorAll('.view-details');
  
  // Exit if no buttons found
  if (detailButtons.length === 0) return;
  
  // Add click event listeners to each button
  detailButtons.forEach(button => {
    button.addEventListener('click', function(e) {
      // Prevent default behavior of anchor links
      e.preventDefault();
      
      // Find the parent game card
      const gameCard = this.closest('.game-card');
      if (!gameCard) return;
      
      // Find the details section to toggle
      const detailsSection = gameCard.querySelector('.game-details-extended');
      if (!detailsSection) return;
      
      // Toggle the visibility of the details section
      if (detailsSection.style.display === 'none' || detailsSection.style.display === '') {
        // Show details
        detailsSection.style.display = 'block';
        
        // Animate the details section
        detailsSection.style.opacity = '0';
        detailsSection.style.maxHeight = '0';
        
        // Trigger animation after a small delay
        setTimeout(() => {
          detailsSection.style.transition = 'opacity 0.3s ease, max-height 0.5s ease';
          detailsSection.style.opacity = '1';
          detailsSection.style.maxHeight = '500px'; // Large enough to fit content
        }, 10);
        
        // Update button text
        this.textContent = 'Hide Details';
      } else {
        // Hide details with animation
        detailsSection.style.opacity = '0';
        detailsSection.style.maxHeight = '0';
        
        // After animation completes, hide the element completely
        setTimeout(() => {
          detailsSection.style.display = 'none';
        }, 300);
        
        // Update button text
        this.textContent = 'View Details';
      }
    });
  });
}

// Add keyboard accessibility for detail toggles
function enhanceAccessibility() {
  const detailButtons = document.querySelectorAll('.view-details');
  
  detailButtons.forEach(button => {
    // Make sure the button can be focused with keyboard
    button.setAttribute('tabindex', '0');
    
    // Add keyboard event listener for Enter and Space keys
    button.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault(); // Prevent default behavior
        this.click(); // Simulate click
      }
    });
  });
} 