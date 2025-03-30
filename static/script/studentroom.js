var panel_name = "student";

$(document).ready(function () {
  debugger;

  var dataTable = $("#studentroomTable").DataTable({
    ajax: "/get_studentroom_list",
    columns: [
      //   { data: "id" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.room.placenumber;
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.room.roomnumber;
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.student.fname + " " + data.student.lname;
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.student.studentid;
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.room.residencetype;
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.room.DormType;
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.student.mobile;
        },
      },
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
