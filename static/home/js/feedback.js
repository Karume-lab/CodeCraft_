const stepMenuOne = document.querySelector('.formbold-step-menu1')
const stepMenuTwo = document.querySelector('.formbold-step-menu2')
const stepMenuThree = document.querySelector('.formbold-step-menu3')

const stepOne = document.querySelector('.formbold-form-step-1')
const stepTwo = document.querySelector('.formbold-form-step-2')
const stepThree = document.querySelector('.formbold-form-step-3')

const formSubmitBtn = document.querySelector('.formbold-btn')
const formBackBtn = document.querySelector('.formbold-back-btn')
const stepThreeBackBtn = document.querySelector('.step-three-back');

let originalButton = formSubmitBtn.innerHTML;


formSubmitBtn.addEventListener("click", function(event){
  event.preventDefault()
  if(stepMenuOne.className == 'formbold-step-menu1 active') {
    event.preventDefault()
    stepMenuOne.classList.remove('active')
    stepMenuTwo.classList.add('active')

    stepOne.classList.remove('active')
    stepTwo.classList.add('active')

    formBackBtn.classList.add('active')
    formBackBtn.addEventListener("click", function (event) {
      event.preventDefault()
      stepMenuOne.classList.add('active')
      stepMenuTwo.classList.remove('active')

      stepOne.classList.add('active')
      stepTwo.classList.remove('active')
      formBackBtn.classList.remove('active')
    })
  } else if (stepMenuTwo.className == 'formbold-step-menu2 active') {
    event.preventDefault();

    stepMenuTwo.classList.remove('active');
    stepMenuThree.classList.add('active');

    stepTwo.classList.remove('active');
    stepThree.classList.add('active');

    formBackBtn.classList.remove('active'); // This line hides the original back button
    stepThreeBackBtn.classList.add('active');
    stepThreeBackBtn.addEventListener('click', function (event) {
        event.preventDefault();
        stepMenuTwo.classList.add('active');
        stepMenuThree.classList.remove('active');
      
        stepTwo.classList.add('active');
        stepThree.classList.remove('active');
      
        // formSubmitBtn.textContent = 'Next Step';
        formSubmitBtn.innerHTML = originalButton;
        stepThreeBackBtn.classList.remove('active'); // Hide stepThreeBackBtn after going back
        formBackBtn.classList.add('active')
    });
    formSubmitBtn.textContent = 'Submit';

} else if(stepMenuThree.className == 'formbold-step-menu3 active') {
        document.querySelector('form').submit()
    }
})