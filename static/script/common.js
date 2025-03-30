function RenderHome() {
  debugger;
  $.ajax({
    url: "/home",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".maindiv").html(result);
    },
    error: function (xhr, status, error) {
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}

function RenderInbox() {
  debugger;
  $.ajax({
    url: "/inbox",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".maindiv").html(result);
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}

function RenderAdvisors() {
  debugger;
  $.ajax({
    url: "/advisors",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);
      $(".table-view").addClass("active");
      $(".details-view").removeClass("active");

      $(".maindiv").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}

function RenderAdvisorDetail(id) {
  debugger;
  var url = "/advisordetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);
      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      renderlinkedStudent();
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderManagerDetail(id) {
  debugger;
  var url = "/managerdetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);
      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      // renderlinkedStudent();
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderInspections() {
  debugger;
  $.ajax({
    url: "/inspection",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);
      $(".table-view").addClass("active");
      $(".details-view").removeClass("active");
      $(".maindiv").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderInspectionsDetail() {
  debugger;
  $.ajax({
    url: "/inspectiondetail",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}

function RenderHalls() {
  debugger;
  $.ajax({
    url: "/halls",
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);
      $(".table-view").addClass("active");
      $(".details-view").removeClass("active");
      $(".maindiv").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderHallsDetail(id) {
  debugger;
  var url = "/halldetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      renderlinkedRooms(id);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderApartmentDetail(id) {
  debugger;
  var url = "/apartmentdetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      // renderlinkedRooms();
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderComplainDetail(id) {
  debugger;
  var url = "/complaindetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderStaffDetail(id) {
  debugger;
  var url = "/staffdetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
function RenderHouseRequestDetail(id) {
  debugger;
  var url = "/houserequestdetail/" + id;
  $.ajax({
    url: url,
    type: "GET",
    contentType: "application/json",
    dataType: "json",
    success: function (result) {
      debugger;
      console.log(result);

      $(".table-view").removeClass("active");
      $(".details-view").addClass("active");

      $(".maintable").remove();
      $(".detailstable").html(result);
      // Advisors();
    },
    error: function (xhr, status, error) {
      debugger;
      debugger;
      console.log(xhr.responseText);
      alert(xhr.responseText);
    },
  });
}
debugger;
// When an image is selected, display a preview
function InitImageContainer() {
  debugger;
}
$("#imagePreview").click(function () {
  $("#imageInput").click();
});
$("#imageInput").change(function () {
  debugger;
  var file = this.files[0];
  if (file) {
    var reader = new FileReader();
    reader.onload = function (event) {
      $("#imagePreview").html(
        '<img src="' +
          event.target.result +
          '" style="max-width: 100%; max-height: 200px;">' +
          `'`
      );
      $(".image-field-header").html(
        $(".image-field-header").html() +
          ` <a id="removeImageButton" class="remove-button" title="Remove Image">&times;</a>`
      );
      InitRemoveButton();
    };
    reader.readAsDataURL(file);
    debugger;
  }
});

function InitRemoveButton() {
  $(document).on("click", ".remove-button", function (event) {
    debugger;
    event.preventDefault();
    $("#imageInput").val(""); // Clear the file input
    var defaultImage =
      '<div class="custom-image-upload">' +
      '<img src="https://du11hjcvx0uqb.cloudfront.net/dist/webpack-production/6dfed94f78923783.svg" alt="Upload Image" class="upload-icon" />' +
      '<div class="upload-text">' +
      "" +
      "<div>Choose a file to upload</div>" +
      "" +
      "</div>" +
      "</div>";
    $(".image-field-header").html('<label for="image">Image:</label>');
    $("#imagePreview").html(defaultImage); // Restore default image preview
  });
}
debugger;
function initformsubmit() {
  debugger;
}
$(document).ready(function () {
  debugger;
  document.getElementById("Form").addEventListener("submit", function (event) {
    // Prevent the default form submission behavior
    event.preventDefault();
    debugger;
    swal({
      title: "Do you want to save?",
      icon: "info",
      buttons: {
        cancel: "No",
        confirm: "Yes",
      },
    }).then((willSave) => {
      if (willSave) {
        var tables = document.querySelectorAll("form table");
        var formData = [];

        // Loop through each table
        tables.forEach(function (table) {
          // Check if the table has an id attribute
          if (table.id) {
            // Retrieve data from the table
            var tableData = RetrieveSource(table.id);
            // If data is retrieved, append it to formData
            if (tableData) {
              formData = formData.concat(tableData);
            }
          }
        });

        // Create a hidden input field to hold the table data
        var tableDataInput = document.createElement("input");
        tableDataInput.type = "hidden";
        tableDataInput.name = "gridJsonData";
        tableDataInput.value = JSON.stringify(formData);

        // Append the hidden input field to the form
        this.appendChild(tableDataInput);

        // Submit the form using AJAX
        var formData = new FormData(this);
        var formAction = this.action;
        var formMethod = this.method;

        fetch(formAction, {
          method: "POST",
          body: formData,
        })
          .then((response) => response.json())
          .then((data) => {
            debugger;
            // Handle the response from the server
            console.log(data);
            if (data.success == true) {
              swal("Success!", data.message, "success").then((value) => {
                RenderHallsDetail(data.id);
                // window.location.href = "/"; // Redirect to home page?
              });
            } else {
              swal("Failed!", data.message, "error").then((value) => {
                RenderHallsDetail(data.id);
                // window.location.href = "/"; // Redirect to home page?
              });
            }

            // Show SweetAlert success message
          })
          .catch((error) => {
            // Handle any errors
            swal("Failed!", data.message, "error").then((value) => {
              RenderHallsDetail(0);
              // window.location.href = "/"; // Redirect to home page?
            });
          });
      } else {
        return;
      }
    });

    // Get all tables in the form
  });
  document
    .getElementById("hallForm")
    .addEventListener("submit", function (event) {
      debugger;
      // Collect data from table rows
      var table = document.getElementById("halllinkedRoomTable");
      var formData = [];

      // Loop through each row (skipping header)
      formData = RetrieveSource("halllinkedRoomTable");
      var tableDataInput = document.createElement("input");
      tableDataInput.type = "hidden";
      tableDataInput.name = "gridJsonData";
      tableDataInput.value = JSON.stringify(formData);

      // Append the hidden input field to the form
      this.appendChild(tableDataInput);
    });
});
function NewFormSubmit(ele) {
  swal({
    title: "Do you want to create New?",
    icon: "info",
    buttons: {
      cancel: "No",
      confirm: "Yes",
    },
  }).then((willSave) => {
    if (willSave) {
      pname = $(ele).attr("panel-name");
      if (pname == "halls") {
        RenderHallsDetail(0);
      }
    } else {
      return;
    }
  });
}

function FormDeleteSubmit(ele) {
  debugger;
  var Id = $(ele).attr("data-id");
  var panelname = $(ele).attr("panel-name");
  var url = "/delete-" + panelname + "/" + Id;
  swal({
    title: "Are you sure?",
    text: "You will not be able to recover this file!",
    icon: "warning",
    buttons: true,
    dangerMode: true,
  }).then((willDelete) => {
    if (willDelete) {
      $.ajax({
        url: url,
        type: "DELETE",
        success: function (data) {
          debugger;
          if (data.success == true) {
            swal("Success!", data.message, "success").then((value) => {
              window.location.reload();

              // window.location.href = "/"; // Redirect to home page?
            });
          } else {
            swal("Failed!", data.message, "error").then((value) => {
              window.location.reload();
            });
          }
        },
        error: function (xhr, status, error) {
          alert(xhr.responseText);
        },
      });
    }
  });
}
function RetrieveSource(gridElement) {
  const table = document.getElementById(gridElement);
  const collectionData = [];

  if (table) {
    const headers = table.querySelectorAll("thead th");
    const headerClasses = Array.from(headers).map(
      (header) => header.classList[0]
    );

    const rows = table.querySelectorAll("tbody tr");
    rows.forEach((row) => {
      const rowData = {};
      const cells = row.querySelectorAll("td");

      headerClasses.forEach((className, index) => {
        rowData[className] = cells[index].innerText;
      });

      collectionData.push(rowData);
    });
  }

  return collectionData;
}
