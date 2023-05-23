let currentStep = 0;
    showStep(currentStep);

    function showStep(n) {
        let steps = document.getElementsByClassName("form-step");
        steps[n].classList.add("active");
    }

    function nextStep(n) {
        let steps = document.getElementsByClassName("form-step");
        if (n == steps.length) {
            document.getElementById("myForm").submit();
            return false;
        }
        steps[currentStep].classList.remove("active");
        steps[currentStep].classList.add("previous");
        currentStep = n;

        let formContainer = document.getElementById("formContainer");
        formContainer.style.transform = `translateX(-${0}%)`;

        showStep(currentStep);
    }

    function prevStep(n) {
      let steps = document.getElementsByClassName("form-step");
      if (n < 0) {
          return false;
      }
      steps[currentStep].classList.remove("active");
      steps[currentStep].classList.remove("previous");
      currentStep = n;

      let formContainer = document.getElementById("formContainer");
      formContainer.style.transform = `translateX(-${0}%)`;

      showStep(currentStep);
    }
    function scrollToForm() {
    document.querySelector('#formContainer').scrollIntoView({ behavior:'smooth' });
}