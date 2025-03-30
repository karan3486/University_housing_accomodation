var panel_name = "staff";

$(document).ready(function () {
  debugger;

  var dataTable = $("#staffsTable").DataTable({
    ajax: "/get_staff_list",
    columns: [
      { data: "staffid" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.fname + " " + data.lname;
        },
      },
      { data: "positionOfStaff" },
      { data: "city" },
      { data: "email" },
      { data: "mobile" },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.staffid +
            '">Edit/View</button>'
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
            data.staffid +
            '">Delete</button>'
          );
        },
      },
    ],
    initComplete: function () {
      InitDeleteAction();
      InitEditAction();
      $(".paginate_button").click(function () {
        InitDeleteAction();
        InitEditAction();
      });
    },
  });
});
