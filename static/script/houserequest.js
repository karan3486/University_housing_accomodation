var panel_name = "houserequest";
$(document).ready(function () {
  debugger;
  var dataTable = $("#houserequestTable").DataTable({
    ajax: "/get_houserequest_list",
    columns: [
      { data: "requestid" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.student.fname + " " + data.student.lname;
        },
      },
      { data: "studentid" },
      { data: "student.email" },
      { data: "student.mobile" },
      { data: "residenceType" },
      { data: "dateofRequest" },
      {
        data: "currentStatus",
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
            data.requestid +
            '">Edit</button>'
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
            data.requestid +
            '">Delete</button>'
          );
        },
      },
    ],
    initComplete: function () {
      debugger;
      InitDeleteAction();
      InitEditAction();
      InitViewAction();
      $(".paginate_button").click(function () {
        InitDeleteAction();
        InitEditAction();
        InitViewAction();
      });
    },
    createdRow: function (row, data, dataIndex) {
      // Add color to the status column only
      var statusCell = $(row).find(".status");
      var statusValue = statusCell.text();
      if (statusValue === "Approved") {
        statusCell.css("background-color", "rgb(126 237 126)");
      } else if (statusValue === "Rejected") {
        statusCell.css("background-color", "rgb(255 92 92)");
      } else if (statusValue === "Pending") {
        statusCell.css("background-color", "rgb(255 255 122)");
      }
      statusCell.css("font-weight", "bolder");
    },
  });
});
function ApproveHouseRequest(ele) {
  debugger;
  var id = $(ele).attr("request-id");
  if (id == undefined || id == "") {
    swal({
      title: "Please select Request id.",
      icon: "info",
    }).then((value) => {
      window.location.reload();
    });
  } else {
    var command = $(ele).attr("command");
    var url = "/approve-houserequest/" + id + "/" + command;
    swal({
      title: "Please confirm you want to " + command + "?",
      text: "The status of this house request will be changed!",
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
                RenderHouseRequestDetail(id);
              });
            } else {
              swal("Rejected!", data.message, "error").then((value) => {
                RenderHouseRequestDetail(id);
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
  // $.ajax({
  //   url: url,
  //   type: "GET",
  //   contentType: "application/json",
  //   dataType: "json",
  //   success: function (result) {
  //     debugger;
  //     console.log(result);
  //     if (result.success == true) {
  //       swal("Success!", data.message, "success");
  //     } else {
  //       swal("Failed!", data.message, "error");
  //     }
  //   },
  //   error: function (xhr, status, error) {
  //     debugger;
  //     debugger;
  //     console.log(xhr.responseText);
  //     alert(xhr.responseText);
  //   },
  // });
}
