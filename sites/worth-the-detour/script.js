const imageDialog = document.querySelector('.image-dialog');
const enlargedImage = imageDialog.querySelector('img');
const imageDialogTitle = document.querySelector('#image-dialog-title');
const interestDialog = document.querySelector('.interest-dialog');
const interestProduct = interestDialog.querySelector('.interest-dialog__product');
const interestForm = interestDialog.querySelector('form');
const emailInput = interestForm.elements.email;
const emailError = document.querySelector('#email-error');
const successMessage = interestDialog.querySelector('.form-success');

function closeOnBackdrop(event) {
  if (event.target === event.currentTarget) event.currentTarget.close();
}

document.querySelectorAll('.product__image-button').forEach((button) => {
  button.addEventListener('click', () => {
    const sourceImage = button.querySelector('img');
    const productName = button.closest('.product').dataset.productName;
    enlargedImage.src = sourceImage.currentSrc || sourceImage.src;
    enlargedImage.alt = sourceImage.alt;
    imageDialogTitle.textContent = productName;
    imageDialog.showModal();
  });
});

document.querySelectorAll('.interest-button').forEach((button) => {
  button.addEventListener('click', () => {
    const product = button.closest('.product');
    interestProduct.textContent = product.dataset.productName;
    interestForm.dataset.designId = product.dataset.designId;
    interestForm.reset();
    interestForm.hidden = false;
    emailError.hidden = true;
    successMessage.hidden = true;
    emailInput.removeAttribute('aria-invalid');
    interestDialog.showModal();
  });
});

imageDialog.querySelector('.image-dialog__close').addEventListener('click', () => imageDialog.close());
interestDialog.querySelector('.interest-dialog__close').addEventListener('click', () => interestDialog.close());
imageDialog.addEventListener('click', closeOnBackdrop);
interestDialog.addEventListener('click', closeOnBackdrop);

interestForm.addEventListener('submit', (event) => {
  event.preventDefault();
  if (!emailInput.validity.valid) {
    emailError.hidden = false;
    emailInput.setAttribute('aria-invalid', 'true');
    emailInput.focus();
    return;
  }

  emailError.hidden = true;
  emailInput.removeAttribute('aria-invalid');
  interestForm.hidden = true;
  successMessage.hidden = false;
  successMessage.focus();
});
