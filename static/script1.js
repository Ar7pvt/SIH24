//   function showMore() {
//     document.getElementById("extra-content").style.display = "block";
//     document.querySelector(".explore-button").style.display = "none";
//   }
function toggleReadMore() {
    const extraContent = document.getElementById("extra-content");
    const button = document.querySelector(".explore-button");

    if (extraContent.style.display === "none") {
      // Show the extra content and change the button text
      extraContent.style.display = "inline";
      button.style.display = "none";

      // Hide the extra content and reset the button after 5 seconds
      setTimeout(() => {
        extraContent.style.display = "none";
        button.style.display = "inline";
      }, 5000);
    }
  }