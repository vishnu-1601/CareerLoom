document.addEventListener('DOMContentLoaded', () => {
    // Dynamic Form Elements
    window.addEducation = function() {
        const container = document.getElementById('education-container');
        const div = document.createElement('div');
        div.className = 'dynamic-group glass-inner';
        div.innerHTML = `
            <button type="button" class="remove-btn" onclick="this.parentElement.remove()">×</button>
            <div class="grid-2-col">
                <div class="input-group"><label>Degree</label><input type="text" name="edu_degree[]" class="input-field"></div>
                <div class="input-group"><label>Institution</label><input type="text" name="edu_institution[]" class="input-field"></div>
                <div class="input-group"><label>Year</label><input type="text" name="edu_year[]" class="input-field"></div>
                <div class="input-group"><label>Score/GPA</label><input type="text" name="edu_score[]" class="input-field"></div>
            </div>
        `;
        container.appendChild(div);
        updateProgress();
    };

    window.addProject = function() {
        const container = document.getElementById('project-container');
        const div = document.createElement('div');
        div.className = 'dynamic-group glass-inner';
        div.innerHTML = `
            <button type="button" class="remove-btn" onclick="this.parentElement.remove()">×</button>
            <div class="input-group"><label>Title</label><input type="text" name="proj_title[]" class="input-field"></div>
            <div class="input-group"><label>Tech Stack</label><input type="text" name="proj_tech[]" class="input-field"></div>
            <div class="input-group"><label>Description</label><textarea name="proj_desc[]" class="input-field"></textarea></div>
        `;
        container.appendChild(div);
        updateProgress();
    };

    window.addExperience = function() {
        const container = document.getElementById('experience-container');
        const div = document.createElement('div');
        div.className = 'dynamic-group glass-inner';
        div.innerHTML = `
            <button type="button" class="remove-btn" onclick="this.parentElement.remove()">×</button>
            <div class="grid-2-col">
                <div class="input-group"><label>Role</label><input type="text" name="exp_role[]" class="input-field"></div>
                <div class="input-group"><label>Company</label><input type="text" name="exp_company[]" class="input-field"></div>
                <div class="input-group"><label>Duration</label><input type="text" name="exp_duration[]" class="input-field"></div>
            </div>
            <div class="input-group"><label>Responsibilities</label><textarea name="exp_resp[]" class="input-field"></textarea></div>
        `;
        container.appendChild(div);
        updateProgress();
    };

    // Progress Bar Logic
    const form = document.getElementById('resume-form');
    const progressBar = document.getElementById('progress-bar');
    
    function updateProgress() {
        if(!form) return;
        const inputs = form.querySelectorAll('input:not([type="button"]):not([type="submit"]), textarea, select');
        let filled = 0;
        let total = inputs.length;
        
        inputs.forEach(input => {
            if (input.value.trim() !== '') {
                filled++;
            }
        });
        
        const percentage = total === 0 ? 0 : Math.round((filled / total) * 100);
        if(progressBar) {
            progressBar.style.width = percentage + '%';
        }
    }

    if(form) {
        form.addEventListener('input', updateProgress);
        // Initial call
        updateProgress();
    }
});
