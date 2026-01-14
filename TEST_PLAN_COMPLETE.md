# Comprehensive Test Plan for Contacts Module

## Test Objective
Validate all functionality of the Contacts module in the ERP application, including creating, reading, updating, and deleting contacts, as well as verifying the display and navigation features.

## Test Scope
- Contact List Display
- Add Contact functionality
- View Contact Details
- Edit Contact functionality  
- Delete Contact functionality
- Form validation and error handling
- Navigation and UI elements

## Test Environment
- **Application URL:** https://v0-erp-application-development-eight.vercel.app/
- **Contacts Page URL:** https://v0-erp-application-development-eight.vercel.app/contacts
- **Browser:** Chromium (Playwright)
- **Testing Framework:** Playwright

---

## TEST SUITE 1: NAVIGATION AND DISPLAY

### Test Case 1.1: Access Contacts Module
**Objective:** Verify user can navigate to the Contacts page

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/
- **Expected Result:** Application loads successfully, dashboard is displayed

Step 2: Click on "Contacts" link in the navigation menu
- **Element:** link "Contacts"
- **Expected Result:** URL changes to /contacts, Contacts page is displayed

Step 3: Verify page title and heading
- **Expected Result:** Page heading displays "Contacts" with subtitle "Manage your business contacts"

Step 4: Verify contacts table is displayed
- **Expected Result:** Table with columns: Name, Email, Phone, Company, Position, Actions is visible

### Test Case 1.2: Verify Initial Contact Data
**Objective:** Verify existing contact is displayed correctly

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Verify contact data in table
- **Expected Result:** Table contains one row with:
  - Name: John Smith
  - Email: john.smith@example.com
  - Phone: +1 (555) 123-4567
  - Company: Acme Corporation
  - Position: Sales Manager

Step 3: Verify action buttons are present
- **Expected Result:** Three action buttons are visible in the Actions column (View, Edit, Delete)

---

## TEST SUITE 2: ADD CONTACT FUNCTIONALITY

### Test Case 2.1: Open Add Contact Dialog
**Objective:** Verify the Add Contact dialog opens correctly

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page is displayed

Step 2: Click on "Add Contact" button
- **Element:** button "Add Contact"
- **Expected Result:** Modal dialog opens with title "Create Contact"

Step 3: Verify dialog content
- **Expected Result:** Dialog displays:
  - Heading: "Create Contact"
  - Subtitle: "Add a new contact to your system."
  - Five input fields: Name, Email, Phone, Company, Position
  - Two buttons: Cancel and Create

Step 4: Verify form field placeholders
- **Expected Result:** 
  - Name field placeholder: "John Doe"
  - Email field placeholder: "john@example.com"
  - Phone field placeholder: "+1 (555) 123-4567"
  - Company field placeholder: "Acme Inc."
  - Position field placeholder: "Sales Manager"

### Test Case 2.2: Create Valid Contact
**Objective:** Successfully create a new contact with valid data

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on "Add Contact" button
- **Expected Result:** Create Contact dialog opens

Step 3: Type "Jane Doe" in Name field
- **Element:** textbox "Name"
- **Expected Result:** Text is entered in Name field

Step 4: Type "jane.doe@example.com" in Email field
- **Element:** textbox "Email"
- **Expected Result:** Text is entered in Email field

Step 5: Type "+1 (555) 987-6543" in Phone field
- **Element:** textbox "Phone"
- **Expected Result:** Text is entered in Phone field

Step 6: Type "Tech Solutions Inc." in Company field
- **Element:** textbox "Company"
- **Expected Result:** Text is entered in Company field

Step 7: Type "Marketing Director" in Position field
- **Element:** textbox "Position"
- **Expected Result:** Text is entered in Position field

Step 8: Click on "Create" button
- **Element:** button "Create"
- **Expected Result:** 
  - Dialog closes
  - New contact appears in the contacts table
  - Success notification may appear

Step 9: Verify new contact in table
- **Expected Result:** Table shows new row with Jane Doe's information

### Test Case 2.3: Cancel Add Contact
**Objective:** Verify cancel functionality discards new contact

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on "Add Contact" button
- **Expected Result:** Create Contact dialog opens

Step 3: Type "Test User" in Name field
- **Expected Result:** Text is entered

Step 4: Type "test@example.com" in Email field
- **Expected Result:** Text is entered

Step 5: Click on "Cancel" button
- **Element:** button "Cancel"
- **Expected Result:** 
  - Dialog closes
  - No new contact is added to the table

Step 6: Verify contact was not created
- **Expected Result:** Test User does not appear in contacts table

### Test Case 2.4: Close Add Contact Dialog
**Objective:** Verify close button (X) functionality

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on "Add Contact" button
- **Expected Result:** Create Contact dialog opens

Step 3: Type "Test User" in Name field
- **Expected Result:** Text is entered

Step 4: Click on "Close" button (X icon)
- **Element:** button "Close"
- **Expected Result:** 
  - Dialog closes
  - No new contact is added

Step 5: Verify contact was not created
- **Expected Result:** Test User does not appear in contacts table

### Test Case 2.5: Create Contact with Empty Fields
**Objective:** Validate required field validation

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on "Add Contact" button
- **Expected Result:** Create Contact dialog opens

Step 3: Leave all fields empty
- **Expected Result:** All fields remain empty

Step 4: Click on "Create" button
- **Expected Result:** Validation error is displayed or form submission is prevented

Step 5: Verify error handling
- **Expected Result:** Appropriate validation messages indicate required fields

### Test Case 2.6: Create Contact with Invalid Email
**Objective:** Validate email format validation

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on "Add Contact" button
- **Expected Result:** Create Contact dialog opens

Step 3: Fill in fields:
- Name: "Test User"
- Email: "invalid-email-format"
- Phone: "+1 (555) 123-4567"
- Company: "Test Corp"
- Position: "Tester"
- **Expected Result:** Fields are filled

Step 4: Click on "Create" button
- **Expected Result:** Email validation error is displayed

Step 5: Verify error handling
- **Expected Result:** Error message indicates invalid email format

### Test Case 2.7: Create Contact with Special Characters
**Objective:** Validate handling of special characters

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on "Add Contact" button
- **Expected Result:** Create Contact dialog opens

Step 3: Enter contact with special characters:
- Name: "O'Brien-Smith Jr."
- Email: "test+tag@example.com"
- Phone: "+1 (555) 123-4567 ext. 890"
- Company: "Smith & Sons, LLC."
- Position: "VP of Sales & Marketing"
- **Expected Result:** All fields accept the input

Step 4: Click on "Create" button
- **Expected Result:** Contact is created successfully

Step 5: Verify special characters are preserved
- **Expected Result:** Contact appears in table with all special characters intact

---

## TEST SUITE 3: VIEW CONTACT DETAILS

### Test Case 3.1: View Existing Contact Details
**Objective:** Verify viewing detailed information of a contact

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads with John Smith contact

Step 2: Click on first action button (View) for John Smith
- **Element:** First button in Actions column
- **Expected Result:** 
  - Navigation to contact detail page
  - URL changes to /contacts/{contact-id}

Step 3: Verify contact detail page content
- **Expected Result:** Page displays:
  - "Back to Contacts" button
  - Contact name as heading: "John Smith"
  - Email: "john.smith@example.com"
  - Phone: "+1 (555) 123-4567"
  - Company: "Acme Corporation"
  - Position: "Sales Manager"

Step 4: Verify Orders section
- **Expected Result:** 
  - Orders heading with count: "0"
  - Message: "No orders found for this contact."

### Test Case 3.2: Navigate Back from Contact Details
**Objective:** Verify back navigation functionality

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on View button for John Smith
- **Expected Result:** Contact detail page is displayed

Step 3: Click on "Back to Contacts" button
- **Element:** button "Back to Contacts"
- **Expected Result:** 
  - Navigation back to contacts list
  - URL changes to /contacts
  - Contacts table is displayed

### Test Case 3.3: Direct URL Access to Contact Details
**Objective:** Verify direct navigation via URL

Step 1: Navigate directly to https://v0-erp-application-development-eight.vercel.app/contacts/87452789-6284-4a43-8ac0-ad3c381e6247
- **Expected Result:** Contact detail page for John Smith loads

Step 2: Verify all contact information is displayed
- **Expected Result:** All contact details are visible and correct

Step 3: Verify "Back to Contacts" button works
- **Expected Result:** Clicking back button returns to contacts list

---

## TEST SUITE 4: EDIT CONTACT FUNCTIONALITY

### Test Case 4.1: Open Edit Contact Dialog
**Objective:** Verify Edit Contact dialog opens with pre-filled data

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on second action button (Edit) for John Smith
- **Element:** Second button in Actions column
- **Expected Result:** Edit Contact dialog opens

Step 3: Verify dialog content and title
- **Expected Result:** 
  - Dialog title: "Edit Contact"
  - Subtitle: "Update the contact information below."

Step 4: Verify pre-filled form fields
- **Expected Result:** Fields contain existing data:
  - Name: "John Smith"
  - Email: "john.smith@example.com"
  - Phone: "+1 (555) 123-4567"
  - Company: "Acme Corporation"
  - Position: "Sales Manager"

Step 5: Verify action buttons
- **Expected Result:** Cancel and Update buttons are present

### Test Case 4.2: Update Contact Information
**Objective:** Successfully update an existing contact

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on Edit button for John Smith
- **Expected Result:** Edit Contact dialog opens

Step 3: Clear and update Name field to "John A. Smith"
- **Element:** textbox "Name"
- **Expected Result:** Name field is updated

Step 4: Clear and update Phone field to "+1 (555) 999-8888"
- **Element:** textbox "Phone"
- **Expected Result:** Phone field is updated

Step 5: Clear and update Position field to "Senior Sales Manager"
- **Element:** textbox "Position"
- **Expected Result:** Position field is updated

Step 6: Click on "Update" button
- **Element:** button "Update"
- **Expected Result:** 
  - Dialog closes
  - Contact information is updated in table

Step 7: Verify updated information
- **Expected Result:** Table shows updated data

### Test Case 4.3: Cancel Edit Contact
**Objective:** Verify cancel preserves original data

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on Edit button for John Smith
- **Expected Result:** Edit Contact dialog opens

Step 3: Change Name field to "Modified Name"
- **Expected Result:** Name field shows new value

Step 4: Click on "Cancel" button
- **Element:** button "Cancel"
- **Expected Result:** Dialog closes

Step 5: Verify original data is preserved
- **Expected Result:** Contact in table shows original name

### Test Case 4.4: Edit Contact with Invalid Email
**Objective:** Validate email format validation during edit

Step 1: Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
- **Expected Result:** Contacts page loads

Step 2: Click on Edit button for John Smith
- **Expected Result:** Edit Contact dialog opens

Step 3: Clear Email field and type "invalid-email"
- **Element:** textbox "Email"
- **Expected Result:** Text is entered

Step 4: Click on "Update" button
- **Expected Result:** Validation error is displayed

Step 5: Verify error handling
- **Expected Result:** Error message indicates invalid email

---

## TEST SUITE 5: DELETE CONTACT FUNCTIONALITY

### Test Case 5.1: Open Delete Confirmation Dialog