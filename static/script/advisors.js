var panel_name = "advisor";
function renderlinkedStudent() {
  var samplestuData = [
    {
      studentName: "karan",
      mobile: "985565545",
      email: "john.doe@example.com",
      roomNumber: "101",
      id: 1,
    },
    {
      studentName: "Sahil",
      mobile: "789562555",
      email: "sahil.doe@example.com",
      roomNumber: "102",
      id: 2,
    },
  ];
  var dataTablestu = $("#advisorstudentTable").DataTable({
    data: samplestuData,
    columns: [
      { data: "id" },
      { data: "studentName" },
      { data: "mobile" },
      { data: "email" },
      { data: "roomNumber" },
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
    ],
    initComplete: function () {
      InitViewAction();
      $(".paginate_button").click(function () {
        InitViewAction();
      });
    },
  });
}

$(document).ready(function () {
  debugger;
  var sampleData = [
    {
      advisorName: "John Doe",
      position: "Professor",
      email: "john.doe@example.com",
      roomNumber: "101",
      contactNumber: "+1234567890",
      departmentName: "Computer Science",
      id: 1,
    },
    {
      advisorName: "Jane Smith",
      position: "Associate Professor",
      email: "jane.smith@example.com",
      roomNumber: "102",
      contactNumber: "+1987654321",
      departmentName: "Engineering",
      id: 2,
    },
    // Add more sample data objects as needed
  ];
  var dataTable = $("#advisorsTable").DataTable({
    ajax: "/get_advisor_list",
    columns: [
      { data: "advisorid" },
      {
        data: null,
        render: function (data, type, row) {
          // Concatenate first and last names
          return data.fname + " " + data.lname;
        },
      },
      { data: "positionOfAdvisor" },
      { data: "email" },
      { data: "roomNo" },
      { data: "mobileNumber" },
      { data: "department" },
      {
        data: null,
        render: function (data, type, row) {
          return (
            '<button  type="button" class="button edit-button" panel-name="' +
            panel_name +
            '" data-id="' +
            data.advisorid +
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
  $("#advisorForm").submit(function (event) {
    event.preventDefault();
    var formData = $(this).serialize();
    // Implement AJAX call to save data
    console.log(formData);
    // Clear form fields after submission
    $(this).trigger("reset");
  });

  // Fill form fields when a record is clicked
  $("#advisorsTable tbody").on("click", "tr", function () {
    debugger;
    var data = dataTable.row(this).data();
    $("#advisorName").val(data.advisorName);
    $("#position").val(data.position);
    $("#email").val(data.email);
    $("#roomNumber").val(data.roomNumber);
    $("#contactNumber").val(data.contactNumber);
    $("#departmentName").val(data.departmentName);
  });
});
