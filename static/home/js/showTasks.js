document.addEventListener('DOMContentLoaded', function() {
	const showTasksButtons = document.querySelectorAll('.btn-show-tasks');

	showTasksButtons.forEach(function(button) {
		button.addEventListener('click', function(event) {
			event.stopPropagation();
			const targetId = button.getAttribute('data-target');
			const targetElement = document.querySelector(targetId);
			targetElement.classList.toggle('show');
		});
	});
});
