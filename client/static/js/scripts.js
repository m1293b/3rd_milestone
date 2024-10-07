// This jQuery add the current year to the footer's paragraph

$("#copyright").text(new Date().getFullYear());

// nav bar made responsive, on smaller screens the site's name disappears, and the little icon becomes the menu button

$(window).on("resize", function () {
  const win = $(this);
  if (win.width() >= 720) {
    $("div.navbar-links-list-div").css("top", "4px");
    $("navbar-brand").html(`
            <a class="brand-in-header" href="#!">No. 39 Recipes</a>
            <div class="cone"></div>`);
  }
  if (win.width() <= 720) {
    $("div.navbar-links-list-div").css("top", "-192px");
    $("navbar-brand").html(`
            <div class="cone"></div>`);
  }
});

// div.cone is the menu button, and this listener controls what happens when the user clicks on it

$("div.cone").on("click", function () {
  if ($("div.navbar-links-list-div").css("top") === "-192px") {
    $("div.navbar-links-list-div").css("top", "64px");
  } else if ($("div.navbar-links-list-div").css("top") === "64px") {
    $("div.navbar-links-list-div").css("top", "-192px");
  }
});

// this listeners control what happens when the user hovers over and then if the mouse leaves any element that has .button as it's class

$(".button").on("mouseover", function () {
  $(this).css("color", "#d2d6db");
  $(this).css("background", "#334155");
});

$(".button").on("mouseleave", function () {
  $(this).css("color", "#334155");
  $(this).css("background", "#d2d6db");
});

// this listeners control what happens when the user clicks on any element that has .delete as it's class

$(".delete").on("click", function () {
  let wrapDiv = $(this).parent();
  let deleteConfirm = wrapDiv.siblings("#delete-confirm");
  wrapDiv.hide();
  deleteConfirm.show();
});

// this listeners control what happens when the user clicks on any element that has .cancel as it's class

$(".cancel").on("click", function () {
  let cardButtons = $(this).parent();
  let wrapDiv = cardButtons.siblings("#card-buttons");
  cardButtons.hide();
  wrapDiv.show();
});