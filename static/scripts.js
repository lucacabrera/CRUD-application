document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("book-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

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
        form.reset();
        form.classList.remove("was-validated");
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
});
