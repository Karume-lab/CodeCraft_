
const modes = document.querySelectorAll('.mode');
const body = document.body;
const sidebar = document.getElementById('accordionSidebar');
const sidebarClasses = {
  default: 'bg-gradient-primary',
  dark: 'dark',
  night: 'bg-gradient-dark'
}
function updateSidebarColor() {
  const bodyColor = body.classList[0];
  sidebar.classList.remove(
	sidebarClasses.default,
	sidebarClasses.dark,
	sidebarClasses.night
  );
  sidebar.classList.add(sidebarClasses[bodyColor]);
}

function handleModeClick(e) {
// remove all existing classes
modes.forEach(mode => {
  body.classList.remove(mode.dataset.mode);
});
body.classList.add(e.target.dataset.mode);
updateSidebarColor();
}
modes.forEach(mode => {
  mode.addEventListener('click', handleModeClick);  
});