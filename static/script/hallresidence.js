var panel_name = "halls";
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
  var dataTable = $("#hallTable").DataTable({
    ajax: "/get_hall_list",
    columns: [
      { data: "hallid" },
      { data: "hallName" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.manager.fname + " " + data.manager.lname;
        },
      },
      { data: "phoneNumber" },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.hallid +
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
            data.hallid +
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
            data.hallid +
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
  debugger;
});
function renderlinkedRooms(id) {
  var dataTableroom = $("#halllinkedRoomTable").DataTable({
    ajax: {
      url: "get-rooms/" + id,
      dataSrc: "data", // Specify "data" as the data source since it's the key containing the array of objects
    },
    columns: [
      {
        data: "room", // Accessing the room object directly
        render: function (data) {
          return data.placenumber; // Render the monthlyRent property of the room object
        },
      },
      { data: "room.roomnumber" }, // Accessing the roomnumber property directly
      { data: "room.monthlyRent" }, // Accessing the monthlyRent property directly
      { data: "room.DormType" }, // Accessing the DormType property directly
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button type="button" class="button delete-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.hallid +
            '">Delete</button>'
          );
        },
      },
    ],
    initComplete: function () {
      InitViewAction();
      $(".paginate_button").click(function () {
        InitViewAction();
      });
    },
  });
}
function openModal() {
  $("#employeeTable").DataTable();
  $("#myModal").css("display", "block");
  // Initialize DataTable
}

// Function to close the modal
function closeModal() {
  $("#myModal").modal("hide");
}
