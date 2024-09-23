$("#copyright").text(new Date().getFullYear());

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

// sign up page input checks

$("input[type=email]").on("change", function (){
  if (!$(this).text().includes('@'))
    console.log('Invalid email address.');
})

$('.button').on('mouseover', function () {
  $(this).css("color","#d2d6db");
  $(this).css("background","#334155");
})

$('.button').on('mouseleave', function () {
  $(this).css("color","#334155");
  $(this).css("background","#d2d6db");
})

$('input[type="password"]').on('change', function () {
  console.log('#yep');
})