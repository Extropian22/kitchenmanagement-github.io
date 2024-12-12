// Intersection Observer for scroll animations
const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
        }
    });
}, observerOptions);

// Observe all elements with animate-on-scroll class
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    animatedElements.forEach(el => observer.observe(el));

    // Initialize number counters
    const statNumbers = document.querySelectorAll('.stat-number');
    statNumbers.forEach(number => {
        const targetNumber = number.innerText;
        const isPercentage = targetNumber.includes('%');
        const numericValue = parseInt(targetNumber);
        
        number.innerText = '0' + (isPercentage ? '%' : '');
        
        let currentNumber = 0;
        const duration = 2000; // 2 seconds
        const steps = 60;
        const increment = numericValue / steps;
        const stepDuration = duration / steps;
        
        const counter = setInterval(() => {
            currentNumber += increment;
            if (currentNumber >= numericValue) {
                currentNumber = numericValue;
                clearInterval(counter);
            }
            number.innerText = Math.round(currentNumber) + (isPercentage ? '%' : '');
        }, stepDuration);
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Parallax effect for hero section
const heroSection = document.querySelector('.hero-section');
if (heroSection) {
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        heroSection.style.backgroundPositionY = scrolled * 0.5 + 'px';
    });
}

// Feature card hover effects
document.querySelectorAll('.feature-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.querySelector('.card-icon').classList.add('bounce');
    });
    
    card.addEventListener('mouseleave', function() {
        this.querySelector('.card-icon').classList.remove('bounce');
    });
});
