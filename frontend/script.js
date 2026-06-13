async function analyzeResume() {

    const fileInput =
        document.getElementById(
            "resumeFile"
        );

    const file =
        fileInput.files[0];

    if (!file) {

        alert(
            "Please upload a resume."
        );

        return;
    }

    const formData =
        new FormData();

    formData.append(
        "file",
        file
    );

    try {

        const response =
            await fetch(
                "http://localhost:8000/analyze",
                {
                    method: "POST",
                    body: formData
                }
            );

        const data =
            await response.json();

        console.log(
            "API Response:",
            data
        );

        // ATS Score

        document.getElementById(
            "atsScore"
        ).innerText =
            data.ats_score + "%";

        // Job Match Score

        document.getElementById(
            "jobMatch"
        ).innerText =
            data.job_match + "%";

        // Predicted Role

        document.getElementById(
            "predictedRole"
        ).innerText =
            data.predicted_role;

        // Skills

        const skillsList =
            document.getElementById(
                "skillsList"
            );

        skillsList.innerHTML = "";

        data.skills.forEach(
            skill => {

                skillsList.innerHTML +=
                    `<li>${skill}</li>`;

            }
        );

        // Suggestions

        const suggestionsList =
            document.getElementById(
                "suggestionsList"
            );

        suggestionsList.innerHTML = "";

        data.suggestions.forEach(
            suggestion => {

                suggestionsList.innerHTML +=
                    `<li>${suggestion}</li>`;

            }
        );

    }
    catch (error) {

        console.error(
            error
        );

        alert(
            "Error analyzing resume. Check backend logs."
        );
    }
}