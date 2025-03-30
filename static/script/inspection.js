var panel_name = "inspection";
$(document).ready(function () {
  debugger;
  var sampleData = [
    {
      staffName: "John Doe",
      dateofInspection: "17.03.2024",
      hallNumber: "23",
      roomNumber: "209",
      address: "47112 Warm Spring blv",
      condition: "Good",
      commments: "All good and no issues",
      id: 1,
    },
    {
      staffName: "Mika Doe",
      dateofInspection: "17.03.2024",
      hallNumber: "25",
      roomNumber: "213",
      address: "27112 Hackamore Spring blv",
      condition: "Bad",
      commments: "Washing machine not working",
      id: 2,
    },
    // Add more sample data objects as needed
  ];
  var dataTable = $("#inspectionsTable").DataTable({
    data: sampleData,
    columns: [
      { data: "id" },
      { data: "staffName" },
      { data: "hallNumber" },
      { data: "roomNumber" },
      { data: "address" },
      { data: "condition" },
      { data: "commments" },
      { data: "dateofInspection" },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.id +
            '">Edit</button>'
          );
        },
      },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button type="button" class="button view-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.id +
            '">View</button>'
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
            data.id +
            '">Delete</button>'
          );
        },
      },
    ],
    initComplete: function () {
      InitDeleteAction();
      InitEditAction();
      InitViewAction();
      $(".paginate_button").click(function () {
        InitDeleteAction();
        InitEditAction();
        InitViewAction();
      });
    },
  });

  // Toggle form section
  $("#toggleFormBtn").click(function () {
    debugger;
    $("#formSection").slideToggle();
  });

  // Form submission
  $("#inspectionForm").submit(function (event) {
    event.preventDefault();
    var formData = $(this).serialize();
    // Implement AJAX call to save data
    console.log(formData);
    // Clear form fields after submission
    $(this).trigger("reset");
  });

  // Fill form fields when a record is clicked
  $("#inspectionsTable tbody").on("click", "tr", function () {
    debugger;
    var data = dataTable.row(this).data();
    $("#staffName").val(data.staffName);
    $("#hall").val(data.hallNumber);
    $("#datetime").val(data.dateofInspection);
    $("#roomNumber").val(data.roomNumber);
    $("#address").val(data.address);
    $("#condition").val(data.condition);
    $("#comments").val(data.commments);
  });
});
