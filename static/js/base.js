$(document).ready(function(){
    // This can be kept empty if you're using pure CSS for movement
});

// This function will scale the image based on the scroll position
window.addEventListener('scroll', function() {
    const image = document.querySelector('.grow-image');
    const scrollPosition = window.scrollY;

    // Set the scale factor; adjust the divisor for speed of growth
    const scale = 1 + scrollPosition / 1000; // Change 1000 to adjust growth speed

    // Apply the scale transformation
    image.style.transform = `scale(${scale})`;
});
