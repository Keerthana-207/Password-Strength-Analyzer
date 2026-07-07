/**
 * LockShield Client Engineering UI Interaction Suite
 */

document.addEventListener('DOMContentLoaded', () => {

    // ---------------------------------------------------------
    // Mobile Responsive Layout Side Navigation Configuration Menu
    // ---------------------------------------------------------
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('open');
            const icon = navToggle.querySelector('i');
            if (navMenu.classList.contains('open')) {
                icon.className = 'fas fa-xmark';
            } else {
                icon.className = 'fas fa-bars';
            }
        });
    }

    // ---------------------------------------------------------
    // Password Mask / Unmask Toggle Visibility Engine
    // ---------------------------------------------------------
    const passwordToggle = document.getElementById('passwordToggle');
    const passwordInput = document.getElementById('password');
    const toggleIcon = document.getElementById('toggleIcon');

    if (passwordToggle && passwordInput && toggleIcon) {
        passwordToggle.addEventListener('click', () => {
            // Evaluates text parameter variations
            const isMasked = passwordInput.getAttribute('type') === 'password';

            if (isMasked) {
                passwordInput.setAttribute('type', 'text');
                toggleIcon.className = 'fas fa-eye-slash';
            } else {
                passwordInput.setAttribute('type', 'password');
                toggleIcon.className = 'fas fa-eye';
            }
        });
    }

    // ---------------------------------------------------------
    // Submission Micro-Interactions & Reset Clear Engine Forms
    // ---------------------------------------------------------
    const analyzerForm = document.getElementById('analyzerForm');
    if (analyzerForm) {
        analyzerForm.addEventListener('submit', (e) => {
            const btnPrimary = analyzerForm.querySelector('.btn-primary');
            if (btnPrimary) {
                btnPrimary.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i> Processing Matrix...';
                btnPrimary.style.pointerEvents = 'none';
                btnPrimary.style.opacity = '0.8';
            }
        });
    }

    // ---------------------------------------------------------
    // Results Page Metric Progress / Scoring Canvas Graphics Animation
    // ---------------------------------------------------------
    const scoreCircle = document.getElementById('scoreCircle');
    const scoreText = document.getElementById('scoreText');
    const resultProgressBar = document.getElementById('resultProgressBar');

    if (scoreCircle && scoreText) {
        // Read native metrics parameters populated during server rendering
        const targetScore = parseInt(scoreCircle.getAttribute('data-score')) || 0;

        // Match status configuration dynamically for programmatic accent mapping
        let activeAccentColor = '#3B82F6'; // default accent blue
        if (targetScore < 40) activeAccentColor = '#EF4444'; // weak red
        else if (targetScore < 70) activeAccentColor = '#F59E0B'; // warn orange
        else if (targetScore <= 100) {
            const summaryBadge = document.querySelector('.badge');
            if (summaryBadge && summaryBadge.classList.contains('status-very-strong')) {
                activeAccentColor = '#22C55E'; // very strong neon green
            }
        }

        let dynamicCount = 0;
        const animationSpeed = 15; // Velocity constant variables values

        if (targetScore === 0) {
            scoreText.textContent = '0';
            scoreCircle.style.background = `conic-gradient(rgba(255, 255, 255, 0.08) 0deg, rgba(255, 255, 255, 0.08) 360deg)`;
        } else {
            const scoreInterval = setInterval(() => {
                dynamicCount++;
                scoreText.textContent = dynamicCount;

                // Conic mapping formula metrics transform degrees values
                const distributionDegrees = (dynamicCount / 100) * 360;
                scoreCircle.style.background = `conic-gradient(
                    ${activeAccentColor} ${distributionDegrees}deg,
                    rgba(255, 255, 255, 0.08) ${distributionDegrees}deg 360deg
                )`;

                if (dynamicCount >= targetScore) {
                    clearInterval(scoreInterval);
                }
            }, animationSpeed);
        }

        // Trigger simultaneous fill for linear horizontal progression lines
        if (resultProgressBar) {
            setTimeout(() => {
                resultProgressBar.style.width = `${targetScore}%`;
            }, 150);
        }
    }
});