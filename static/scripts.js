src =
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js";
integrity =
  "sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r";
crossorigin = "anonymous";

src = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.min.js";
integrity =
  "sha384-7qAoOXltbVP82dhxHAUje59V5r2YsVfBafyUDxEdApLPmcdhBPg1DKg1ERo0BZlK";
crossorigin = "anonymous";

document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("book-form");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    if (!form.checkValidity()) {
      form.classList.add("was-validated");
      return;
    }

    const formData = new FormData(form);
    const data = {
      title: formData.get("title"),
      author: formData.get("author"),
      published_date: formData.get("published_date"),
    };

    fetch("/books", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((result) => {
        alert("book added");
        form.reset();
        form.classList.remove("was-validated");
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("failed to add book");
      });
  });
});
