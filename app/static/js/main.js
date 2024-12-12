// Main JavaScript file for Kitchen Manager Pro

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    initializeTooltips();
    
    // Setup alert dismissal
    setupAlertDismissal();
    
    // Setup form validation
    setupFormValidation();
    
    // Initialize dynamic data updates
    initializeDynamicUpdates();
});

// Initialize tooltips
function initializeTooltips() {
    const tooltips = document.querySelectorAll('[data-tooltip]');
    tooltips.forEach(tooltip => {
        tooltip.addEventListener('mouseenter', (e) => {
            const tip = document.createElement('div');
            tip.className = 'tooltip';
            tip.textContent = e.target.dataset.tooltip;
            document.body.appendChild(tip);
            
            const rect = e.target.getBoundingClientRect();
            tip.style.top = rect.bottom + 5 + 'px';
            tip.style.left = rect.left + (rect.width - tip.offsetWidth) / 2 + 'px';
        });
        
        tooltip.addEventListener('mouseleave', () => {
            const tips = document.querySelectorAll('.tooltip');
            tips.forEach(tip => tip.remove());
        });
    });
}

// Setup alert dismissal
function setupAlertDismissal() {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        if (!alert.classList.contains('alert-persistent')) {
            setTimeout(() => {
                alert.style.opacity = '0';
                setTimeout(() => alert.remove(), 300);
            }, 5000);
        }
    });
}

// Setup form validation
function setupFormValidation() {
    const forms = document.querySelectorAll('form[data-validate]');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            if (!validateForm(form)) {
                e.preventDefault();
            }
        });
    });
}

// Form validation helper
function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input[required], select[required], textarea[required]');
    
    inputs.forEach(input => {
        if (!input.value.trim()) {
            isValid = false;
            showError(input, 'This field is required');
        } else {
            clearError(input);
        }
    });
    
    return isValid;
}

// Show error message
function showError(element, message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    
    const existing = element.parentElement.querySelector('.error-message');
    if (existing) {
        existing.remove();
    }
    
    element.parentElement.appendChild(errorDiv);
    element.classList.add('error');
}

// Clear error message
function clearError(element) {
    const errorDiv = element.parentElement.querySelector('.error-message');
    if (errorDiv) {
        errorDiv.remove();
    }
    element.classList.remove('error');
}

// Initialize dynamic updates
function initializeDynamicUpdates() {
    // Update dashboard statistics periodically
    if (document.querySelector('.dashboard')) {
        setInterval(updateDashboardStats, 60000); // Update every minute
    }
}

// Update dashboard statistics
async function updateDashboardStats() {
    try {
        const response = await fetch('/api/dashboard/stats');
        if (!response.ok) throw new Error('Failed to fetch dashboard stats');
        
        const data = await response.json();
        updateDashboardCards(data);
    } catch (error) {
        console.error('Error updating dashboard stats:', error);
    }
}

// Update dashboard cards with new data
function updateDashboardCards(data) {
    const cards = document.querySelectorAll('.dashboard-card');
    cards.forEach(card => {
        const key = card.dataset.stat;
        if (data[key]) {
            const numberElement = card.querySelector('.card-number');
            if (numberElement) {
                numberElement.textContent = data[key];
            }
        }
    });
}

// Handle AJAX form submissions
function handleAjaxForm(formElement, successCallback) {
    formElement.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        try {
            const formData = new FormData(formElement);
            const response = await fetch(formElement.action, {
                method: formElement.method,
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            
            if (!response.ok) throw new Error('Form submission failed');
            
            const data = await response.json();
            if (successCallback) successCallback(data);
            
        } catch (error) {
            console.error('Error submitting form:', error);
            showError(formElement, 'An error occurred while submitting the form');
        }
    });
}

// Export functions for use in other modules
window.KitchenManager = {
    handleAjaxForm,
    showError,
    clearError,
    validateForm
};
