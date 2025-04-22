/**
 * game-filter.js
 * Provides functionality for filtering and searching games in the catalog
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
  // Initialize the game filter functionality
  initGameFilter();
});

/**
 * Initialize game filtering functionality
 */
function initGameFilter() {
  const searchInput = document.getElementById('game-search');
  const genreFilter = document.getElementById('genre-filter');
  const platformFilter = document.getElementById('platform-filter');
  const yearFilter = document.getElementById('year-filter');
  const resetFiltersBtn = document.getElementById('reset-filters');
  const gameCards = document.querySelectorAll('.game-card');
  
  // Exit if filter elements don't exist (e.g., not on the games page)
  if (!searchInput && !genreFilter && !platformFilter) return;
  
  // Initialize filter counters
  updateFilterCounts();
  
  // Search input event listener (live search)
  if (searchInput) {
    searchInput.addEventListener('input', applyFilters);
  }
  
  // Filter dropdown event listeners
  if (genreFilter) {
    genreFilter.addEventListener('change', applyFilters);
  }
  
  if (platformFilter) {
    platformFilter.addEventListener('change', applyFilters);
  }
  
  if (yearFilter) {
    yearFilter.addEventListener('change', applyFilters);
  }
  
  // Reset filters button event listener
  if (resetFiltersBtn) {
    resetFiltersBtn.addEventListener('click', function() {
      if (searchInput) searchInput.value = '';
      if (genreFilter) genreFilter.value = '';
      if (platformFilter) platformFilter.value = '';
      if (yearFilter) yearFilter.value = '';
      
      applyFilters();
    });
  }
  
  /**
   * Apply all filters to the game cards
   */
  function applyFilters() {
    const searchTerm = searchInput ? searchInput.value.toLowerCase().trim() : '';
    const selectedGenre = genreFilter ? genreFilter.value : '';
    const selectedPlatform = platformFilter ? platformFilter.value : '';
    const selectedYear = yearFilter ? yearFilter.value : '';
    
    let visibleCount = 0;
    
    gameCards.forEach(card => {
      const title = card.querySelector('.game-title').textContent.toLowerCase();
      const description = card.querySelector('.game-description') ? 
        card.querySelector('.game-description').textContent.toLowerCase() : '';
      const genre = card.dataset.genre || '';
      const platform = card.dataset.platform || '';
      const year = card.dataset.year || '';
      
      // Apply search filter
      const matchesSearch = searchTerm === '' || 
        title.includes(searchTerm) || 
        description.includes(searchTerm);
      
      // Apply genre filter
      const matchesGenre = selectedGenre === '' || genre === selectedGenre;
      
      // Apply platform filter
      const matchesPlatform = selectedPlatform === '' || platform === selectedPlatform;
      
      // Apply year filter
      const matchesYear = selectedYear === '' || year === selectedYear;
      
      // Only show card if it matches all active filters
      const isVisible = matchesSearch && matchesGenre && matchesPlatform && matchesYear;
      
      // Update card visibility
      card.style.display = isVisible ? 'block' : 'none';
      
      // Count visible cards
      if (isVisible) visibleCount++;
    });
    
    // Update "no results" message
    updateNoResultsMessage(visibleCount);
    
    // Update filter counts after applying filters
    updateFilterCounts();
  }
  
  /**
   * Update the filter dropdown counts to show number of games in each category
   */
  function updateFilterCounts() {
    // Update genre counts
    if (genreFilter) {
      const genreOptions = genreFilter.querySelectorAll('option');
      genreOptions.forEach(option => {
        if (option.value === '') return; // Skip "All" option
        
        const genre = option.value;
        const count = countVisibleCardsByAttribute('data-genre', genre);
        option.textContent = `${option.getAttribute('data-name')} (${count})`;
      });
    }
    
    // Update platform counts
    if (platformFilter) {
      const platformOptions = platformFilter.querySelectorAll('option');
      platformOptions.forEach(option => {
        if (option.value === '') return; // Skip "All" option
        
        const platform = option.value;
        const count = countVisibleCardsByAttribute('data-platform', platform);
        option.textContent = `${option.getAttribute('data-name')} (${count})`;
      });
    }
    
    // Update year counts
    if (yearFilter) {
      const yearOptions = yearFilter.querySelectorAll('option');
      yearOptions.forEach(option => {
        if (option.value === '') return; // Skip "All" option
        
        const year = option.value;
        const count = countVisibleCardsByAttribute('data-year', year);
        option.textContent = `${option.getAttribute('data-name')} (${count})`;
      });
    }
  }
  
  /**
   * Count visible cards that match a specific attribute value
   */
  function countVisibleCardsByAttribute(attribute, value) {
    let count = 0;
    gameCards.forEach(card => {
      if (card.style.display !== 'none' && card.getAttribute(attribute) === value) {
        count++;
      }
    });
    return count;
  }
  
  /**
   * Show or hide the "no results" message based on visible card count
   */
  function updateNoResultsMessage(visibleCount) {
    let noResultsMsg = document.querySelector('.no-results-message');
    
    if (visibleCount === 0) {
      if (!noResultsMsg) {
        noResultsMsg = document.createElement('div');
        noResultsMsg.className = 'no-results-message';
        noResultsMsg.innerHTML = `
          <p>No games match your filters.</p>
          <button class="reset-btn">Reset Filters</button>
        `;
        
        const gamesContainer = document.querySelector('.game-grid');
        gamesContainer.appendChild(noResultsMsg);
        
        // Add event listener to the reset button
        noResultsMsg.querySelector('.reset-btn').addEventListener('click', function() {
          if (resetFiltersBtn) resetFiltersBtn.click();
        });
      }
    } else if (noResultsMsg) {
      noResultsMsg.remove();
    }
  }
} 