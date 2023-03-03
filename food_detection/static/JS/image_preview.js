const pictureInput = document.getElementById('picture');
const picturePreview = document.getElementById('picturePreview');

pictureInput.addEventListener('change', function() {
  const file = this.files[0];

  if (file.type.startsWith('image/')) {
    const reader = new FileReader();

    reader.onload = function() {
      picturePreview.src = reader.result;
    };

    reader.readAsDataURL(file);
  }
});
