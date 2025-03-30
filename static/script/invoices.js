var panel_name = "student";

$(document).ready(function () {
  debugger;

  var dataTable = $("#invoicesTable").DataTable({
    ajax: "/get_invoice_list",
    columns: [
      { data: "invoiceid" },
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
          return data.student.fname + " " + data.student.lname;
        },
      },
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
          return data.student.email;
        },
      },
      { data: "paymentDate" },
      { data: "methodOfPayment" },
      { data: "totalamount" },
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
