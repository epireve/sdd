/**
 * animation.js
 * Adds smooth animations and transitions to the GameRevs website
 */

document.addEventListener('DOMContentLoaded', function() {
  // Initialize all animations
  initAnimations();
});

/**
 * Set up all animations for the website
 */
function initAnimations() {
  // Add fade-in animations to game cards
  animateGameCards();
  
  // Add smooth scrolling for anchor links
  initSmoothScrolling();
  
  // Add hover animations for navigation
  initNavHoverEffects();
  
  // Add content reveal animations on scroll
  initScrollReveal();
}

/**
 * Add staggered fade-in animations to game cards
 */
function animateGameCards() {
  const gameCards = document.querySelectorAll('.game-card');
  
  if (gameCards.length === 0) return;
  
  // Add animation classes to each card with staggered delay
  gameCards.forEach((card, index) => {
    // Add initial invisible state
    card.classList.add('animate-card');
    card.style.opacity = '0';
    card.style.transform = 'translateY(20px)';
    
    // Set staggered animation delay based on index
    const delay = 100 + (index * 50); // 100ms base delay + 50ms per card
    
    // Trigger animation after a small delay
    setTimeout(() => {
      card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      card.style.opacity = '1';
      card.style.transform = 'translateY(0)';
    }, delay);
  });
}

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
  const anchors = document.querySelectorAll('a[href^="#"]:not([href="#"])');
  
  anchors.forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      
      const targetId = this.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      
      if (targetElement) {
        // Get the target's position relative to the viewport
        const rect = targetElement.getBoundingClientRect();
        // Get the current scroll position
        const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
        // Calculate the target position
        const targetPosition = rect.top + scrollTop - 80; // 80px offset for header
        
        // Smooth scroll to target
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

/**
 * Add hover effects to navigation items
 */
function initNavHoverEffects() {
  const navItems = document.querySelectorAll('.nav-item');
  
  navItems.forEach(item => {
    item.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-2px)';
    });
    
    item.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
}

/**
 * Reveal elements as they scroll into view
 */
function initScrollReveal() {
  // Elements to reveal on scroll
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  
  if (revealElements.length === 0) return;
  
  // Set initial state for all elements
  revealElements.forEach(el => {
    el.classList.add('hidden-element');
  });
  
  // Check element visibility on scroll
  function checkVisibility() {
    revealElements.forEach(el => {
      if (isElementInViewport(el) && el.classList.contains('hidden-element')) {
        el.classList.remove('hidden-element');
        el.classList.add('revealed-element');
      }
    });
  }
  
  // Initial check on page load
  checkVisibility();
  
  // Check on scroll
  window.addEventListener('scroll', checkVisibility);
  
  // Helper function to check if element is in viewport
  function isElementInViewport(el) {
    const rect = el.getBoundingClientRect();
    return (
      rect.top <= (window.innerHeight || document.documentElement.clientHeight) * 0.8 && 
      rect.bottom >= 0
    );
  }
}

// Add animation styles to the document
function addAnimationStyles() {
  const styleSheet = document.createElement('style');
  styleSheet.type = 'text/css';
  styleSheet.innerText = `
    .animate-card {
      transition: opacity 0.5s ease, transform 0.5s ease;
    }
    
    .hidden-element {
      opacity: 0;
      transform: translateY(30px);
      transition: opacity 0.8s ease, transform 0.8s ease;
    }
    
    .revealed-element {
      opacity: 1;
      transform: translateY(0);
    }
    
    .nav-item {
      transition: transform 0.2s ease;
    }
    
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes slideInRight {
      from { opacity: 0; transform: translateX(50px); }
      to { opacity: 1; transform: translateX(0); }
    }
    
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.05); }
      100% { transform: scale(1); }
    }
    
    .fade-in {
      animation: fadeIn 0.8s ease forwards;
    }
    
    .slide-in-right {
      animation: slideInRight 0.8s ease forwards;
    }
    
    .pulse {
      animation: pulse 2s infinite;
    }
  `;
  
  document.head.appendChild(styleSheet);
}

// Add animation styles to document head
addAnimationStyles(); 