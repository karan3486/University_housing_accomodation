var panel_name = "apartment";
$(document).ready(function () {
  debugger;
  initformsubmit();
  var sampleData = [
    {
      hallName: "hAcknmore Doe",
      manager: "Karan Shrestha",
      telephone: "6577523",
      id: 1,
    },
    {
      hallName: "AKTU Doe",
      manager: "Rahul Kumar",
      telephone: "8577523",
      id: 2,
    },
    // Add more sample data objects as needed
  ];
  var dataTable = $("#apartmentsTable").DataTable({
    ajax: "/get_apartment_list",
    columns: [
      { data: "appartmentid" },
      { data: "apartmentname" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.manager.fname + " " + data.manager.lname;
        },
      },
      { data: "telephone" },
      { data: "capacity" },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.appartmentid +
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
            data.appartmentid +
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
