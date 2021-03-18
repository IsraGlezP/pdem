$(document).ready(function(){
    $('.slider').slick({
        dots: true,
        appendArrows: $(".nav-arrows"),
        arrows: true,
        infinite: false,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        responsive: [
            {
                breakpoint: 1400,
                settings: {
                    slidesToShow: 4,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 1200,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
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
