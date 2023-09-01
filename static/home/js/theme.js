const modes = document.querySelectorAll('.mode');
const body = document.body;
const sidebar = document.getElementById('accordionSidebar');
const searchbar = document.getElementById('searchBar');

const sidebarClasses = {
  default: 'bg-gradient-primary',
  dark: 'grey-accordion',
  night: 'black-accordion'
};

function updateSidebarColor() {
  const theme = body.classList.contains('sidebar-toggled')
  ? body.classList[1]
  : body.classList[0];
  
  searchbar.classList.remove(
    'bg-white',
    sidebarClasses.default,
    sidebarClasses.dark,
    sidebarClasses.night
  );

  sidebar.classList.remove(
	sidebarClasses.default,
	sidebarClasses.dark,
	sidebarClasses.night
  );
  if (theme === 'default') {
    searchbar.classList.add('bg-white');
  } else {
    searchbar.classList.add(sidebarClasses[theme]);
  }  
  sidebar.classList.add(sidebarClasses[theme]);
}

function saveTheme(theme) {
  localStorage.setItem('theme', theme);
}

function loadTheme() {
  const loadedTheme = localStorage.getItem('theme');
  body.classList.remove('hidden-content');
  if (loadedTheme && !body.classList.contains(loadedTheme)) {
    body.classList.add(loadedTheme);
    updateSidebarColor();
  }
}

function handleModeClick(e) {
  const theme = e.target.dataset.mode;
    // remove all existing classes
  modes.forEach(mode => {
    body.classList.remove(mode.dataset.mode);
  });
  body.classList.add(e.target.dataset.mode);
  updateSidebarColor();
  saveTheme(theme);
  }
  
  loadTheme();
  modes.forEach(mode => {
    mode.addEventListener('click', handleModeClick);  
    
  });
  
document.addEventListener('DOMContentLoaded', loadTheme);