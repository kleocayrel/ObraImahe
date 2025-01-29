<script>
function previewFile(input) {
    const preview = document.getElementById('imagePreview'); // Image element for preview
    const file = input.files[0]; // Get the first file selected

    if (file) {
        const reader = new FileReader(); // FileReader to read the file content

        // When the file is fully loaded
        reader.onload = function (event) {
            preview.src = event.target.result; // Set the image source to the file's content
            preview.style.display = 'block'; // Display the image
        };

        // Read the file as a data URL
        reader.readAsDataURL(file);
    } else {
        // If no file is selected, reset the preview
        preview.src = '';
        preview.style.display = 'none';
    }
}
</script>