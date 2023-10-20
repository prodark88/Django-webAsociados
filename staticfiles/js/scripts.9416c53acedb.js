$(document).ready(function () {
    var currentIndex = 0;
    var images = [
        "../static/img/portada.png",
        "../static/img/pichari.png",
        "../static/img/ayacucho2.png",
    ];

    function showImage(index) {
      $("#portada-img").attr("src", images[index]);
    }

    $("#arrow-left").click(function () {
      currentIndex = (currentIndex - 1 + images.length) % images.length;
      showImage(currentIndex);
    });

    $("#arrow-right").click(function () {
      currentIndex = (currentIndex + 1) % images.length;
      showImage(currentIndex);
    });

    // Cambio automático cada 3 segundos
    setInterval(function () {
      currentIndex = (currentIndex + 1) % images.length;
      showImage(currentIndex);
    }, 4500);
  });   