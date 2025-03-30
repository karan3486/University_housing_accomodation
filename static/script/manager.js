var panel_name = "manager";
$(document).ready(function () {
  debugger;
  var dataTable = $("#managersTable").DataTable({
    ajax: "/get_manager_list",
    columns: [
      { data: "managerid" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.fname + " " + data.lname;
        },
      },
      { data: "email" },
      { data: "mobile" },
      { data: "gender" },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.managerid +
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
      $(".paginate_button").click(function () {
        InitDeleteAction();
        InitEditAction();
      });
    },
  });
});
