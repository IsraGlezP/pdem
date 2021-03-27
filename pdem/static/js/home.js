$(document).ready(function(){
    $('.slider').slick({
        dots: true,
        appendDots: $(".dots"),
        infinite: true,
        speed: 300,
        slidesToShow: 3,
        slidesToScroll: 1,
        nextArrow: $(".next"),
        prevArrow: $(".prev"),
        responsive: [
            {
                breakpoint: 1400,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            },
        ]
    });       
});

// Intersection Observer API
const images = document.querySelectorAll('.anim');

const observer = new IntersectionObserver((entries) => {

    entries.forEach(entry => {
        if(entry.intersectionRatio > 0) {
            entry.target.style.animation = `anim1 0.7s ${entry.target.dataset.delay} forwards ease-out`;
            observer.unobserve(entry.target);
        }
        else {
            entry.target.style.animation = 'none';
        }
    });

});

images.forEach(image => {
    observer.observe(image)
});
