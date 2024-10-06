$("#copyright").text(new Date().getFullYear());

let messages = [];

// nav bar made responsive

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

$("div.cone").on("click", function () {
  if ($("div.navbar-links-list-div").css("top") === "-192px") {
    $("div.navbar-links-list-div").css("top", "64px");
  } else if ($("div.navbar-links-list-div").css("top") === "64px") {
    $("div.navbar-links-list-div").css("top", "-192px");
  }
});

// sign up page input checks to be updated

$("input[type=email]").on("change", function () {
  if (!$(this).text().includes("@")) messages.push("Invalid email address.");
});

$(".button").on("mouseover", function () {
  $(this).css("color", "#d2d6db");
  $(this).css("background", "#334155");
});

$(".button").on("mouseleave", function () {
  $(this).css("color", "#334155");
  $(this).css("background", "#d2d6db");
});

$('input[type="password"]').on("change", function () {
  console.log("#yep");
});

$(".delete").click(deleteConfirm);

function deleteConfirm() {
  let recipeId = $(this).siblings('input[type="hidden"]').attr("value");
  let wrapDiv = $(this).closest("form").parent();
  let wrapDivHtml = $(this).closest("form").parent().html();

  wrapDiv.html(`
    <form action="{{ url_for('delete_recipe')}}" method="POST" class="px-1 mr-1 tablet:mr-0">
        <input type="hidden" value="${recipeId}" name='selected_recipe'>
        <input type="submit" name="delete" id="delete_recipe" value="Confirm" class="delete">
    </form>
    <button class="bg-red justify-self-center px-1" name="cancel" id="cancel">
        <b>X</b>
    </button>
    </form>
    `);
  $("#cancel").on("click", function () {
    wrapDiv.html(wrapDivHtml);
  });
  $(".delete").on("click", deleteConfirm());
}
