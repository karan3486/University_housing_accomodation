var panel_name = "student";

$(document).ready(function () {
  debugger;

  var dataTable = $("#studentsTable").DataTable({
    ajax: "/get_student_list",
    columns: [
      { data: "studentid" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.fname + " " + data.lname;
        },
      },
      { data: "trimester" },
      { data: "mobile" },
      { data: "email" },
      { data: "gender" },
      { data: "nationality" },
      { data: "major" },
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
