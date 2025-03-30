var panel_name = "complain";
$(document).ready(function () {
  debugger;
  var dataTable = $("#complainTable").DataTable({
    ajax: "/get_complain_list",
    columns: [
      { data: "complainid" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.student.fname + " " + data.student.lname;
        },
      },
      { data: "dateofComplain" },
      { data: "comments" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          if (data.staff != undefined)
            return data.staff.fname + " " + data.staff.lname;
          else return "NA";
        },
      },
      { data: "dateofResolved" },
      {
        data: "statusOfCompalin",
        className: "status", // Add class name to the currentStatus column
        render: function (data, type, row) {
          return data; // Return the status value
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.complainid +
            '">Edit-View</button>'
          );
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button type="button" class="button delete-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.complainid +
            '">Delete</button>'
          );
        },
      },
    ],
    initComplete: function () {
      debugger;
      InitDeleteAction();
      InitEditAction();
      $(".paginate_button").click(function () {
        InitDeleteAction();
        InitEditAction();
      });
    },
    createdRow: function (row, data, dataIndex) {
      // Add color to the status column only
      var statusCell = $(row).find(".status");
      var statusValue = statusCell.text();
      if (statusValue === "Resolved") {
        statusCell.css("background-color", "rgb(126 237 126)");
      } else if (statusValue === "Pending") {
        statusCell.css("background-color", "rgb(255 92 92)");
      } else if (statusValue === "Inprogress") {
        statusCell.css("background-color", "rgb(255 255 122)");
      }
      statusCell.css("font-weight", "bolder");
    },
  });
});
function MarkComplainStatus(ele) {
  debugger;
  var id = $(ele).attr("request-id");
  if (id == undefined || id == "") {
    swal({
      title: "Please select Complain id.",
      icon: "info",
    }).then((value) => {
      window.location.reload();
    });
  } else {
    var command = $(ele).attr("command");
    var url = "/approve-complain/" + id + "/" + command;
    swal({
      title: "Please confirm you want to " + command + "?",
      text: "The status of this complain will be changed!",
      icon: "info",
      buttons: true,
    }).then((willDelete) => {
      if (willDelete) {
        $.ajax({
          url: url,
          type: "GET",
          success: function (data) {
            debugger;
            if (data.success == true) {
              swal("Success!", data.message, "success").then((value) => {
                RenderComplainDetail(id);
              });
            } else {
              swal("Failed!", data.message, "error").then((value) => {
                RenderComplainDetail(id);
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
}
