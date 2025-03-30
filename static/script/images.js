$("#imageInput").change(function () {
  debugger;
  var file = this.files[0];
  if (file) {
    var reader = new FileReader();
    reader.onload = function (event) {
      $("#imagePreview").html(
        '<img src="' +
          event.target.result +
          '" style="max-width: 100%; max-height: 200px;">'
      );
    };
    reader.readAsDataURL(file);
  }
});
