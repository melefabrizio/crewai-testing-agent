# Test Plan: Contacts Module - ERP Application

## Test Objective
To comprehensively test all features and functionality of the Contacts module in the ERP application, ensuring that users can successfully create, read, update, and delete contacts, and that all validations and error handling work as expected.

## Scope
- Contact listing and display
- Contact creation (Add Contact)
- Contact viewing (View details)
- Contact editing (Update Contact)
- Contact deletion with confirmation
- Form validation and error handling
- Navigation and user experience
- Data persistence and integrity

## Test Environment
- **Application URL**: https://v0-erp-application-development-eight.vercel.app/
- **Target Module**: Contacts (/contacts)
- **Browser**: Chromium (via Playwright)

---

## Test Suite 1: Navigation and Page Load

### Test Case 1.1: Navigate to Contacts Page from Dashboard
**Objective**: Verify that users can navigate to the Contacts page from the main navigation

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/
2. Verify that the Dashboard page loads successfully
3. Click on the "Contacts" link in the navigation menu (CSS selector: `a[href="/contacts"]`)
4. Wait for the page to load

**Expected Results**:
- URL changes to https://v0-erp-application-development-eight.vercel.app/contacts
- Page title remains "ERP Demo"
- "Contacts" heading (level 1) is displayed
- Subtitle "Manage your business contacts" is visible
- "Add Contact" button is displayed
- Contacts table with headers (Name, Email, Phone, Company, Position, Actions) is visible
- At least one contact (John Smith) is displayed in the table

### Test Case 1.2: Verify Contacts Page Elements
**Objective**: Verify that all page elements are correctly displayed

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Take a snapshot of the page to verify element structure

**Expected Results**:
- Page heading "Contacts" is displayed
- Subtitle "Manage your business contacts" is visible
- "Add Contact" button with icon is present and clickable
- Table structure contains 6 columns: Name, Email, Phone, Company, Position, Actions
- Each contact row has 3 action buttons (View, Edit, Delete)
- Navigation menu shows "Contacts" as the active page

---

## Test Suite 2: View Contact List

### Test Case 2.1: Display Existing Contacts
**Objective**: Verify that existing contacts are displayed correctly in the table

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Locate the contacts table
3. Verify the contact data for "John Smith"

**Expected Results**:
- Contact row displays:
  - Name: "John Smith"
  - Email: "john.smith@example.com"
  - Phone: "+1 (555) 123-4567"
  - Company: "Acme Corporation"
  - Position: "Sales Manager"
- Three action buttons are visible in the Actions column

### Test Case 2.2: Verify Table Structure
**Objective**: Ensure table headers and structure are correct

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Verify table headers

**Expected Results**:
- Table contains headers: Name, Email, Phone, Company, Position, Actions
- Headers are clearly visible and properly aligned
- Table is responsive and displays correctly

---

## Test Suite 3: Add New Contact

### Test Case 3.1: Open Add Contact Dialog
**Objective**: Verify that the Add Contact dialog opens correctly

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button (CSS selector: `button:has-text("Add Contact")`)
3. Wait for dialog to appear

**Expected Results**:
- Dialog with title "Create Contact" appears
- Subtitle "Add a new contact to your system." is displayed
- Form contains 5 fields with placeholders:
  - Name textbox (placeholder: "John Doe")
  - Email textbox (placeholder: "john@example.com")
  - Phone textbox (placeholder: "+1 (555) 123-4567")
  - Company textbox (placeholder: "Acme Inc.")
  - Position textbox (placeholder: "Sales Manager")
- "Cancel" button is present
- "Create" button is present
- Close button (X) is visible in dialog header

### Test Case 3.2: Create Contact with Valid Data
**Objective**: Successfully create a new contact with all required fields

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Wait for dialog to appear
4. Fill in the Name field with "Jane Doe"
5. Fill in the Email field with "jane.doe@example.com"
6. Fill in the Phone field with "+1 (555) 987-6543"
7. Fill in the Company field with "Tech Solutions Inc."
8. Fill in the Position field with "Marketing Director"
9. Click "Create" button
10. Wait for the dialog to close

**Expected Results**:
- Dialog closes successfully
- New contact "Jane Doe" appears in the contacts table
- Contact data is displayed correctly in all columns
- Success message or notification may appear (if implemented)
- Contact count increases

### Test Case 3.3: Cancel Contact Creation
**Objective**: Verify that canceling the dialog discards entered data

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in the Name field with "Test User"
4. Fill in the Email field with "test@example.com"
5. Click "Cancel" button
6. Verify the contacts list

**Expected Results**:
- Dialog closes
- No new contact "Test User" is created
- Contacts list remains unchanged
- No data is saved

### Test Case 3.4: Close Dialog Using X Button
**Objective**: Verify that closing the dialog via X button works correctly

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in some fields with test data
4. Click the Close button (X) in dialog header
5. Verify the contacts list

**Expected Results**:
- Dialog closes
- No new contact is created
- Form data is not saved

### Test Case 3.5: Create Contact with Minimum Data
**Objective**: Test contact creation with only required fields

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in only the Name field with "Minimal Contact"
4. Leave other fields empty
5. Click "Create" button

**Expected Results**:
- If all fields are required: validation error messages appear for empty fields
- If only some fields are required: contact is created with partial data
- Appropriate error handling or success message is displayed

### Test Case 3.6: Create Contact with Invalid Email
**Objective**: Verify email validation

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in the Name field with "Invalid Email User"
4. Fill in the Email field with "notanemail" (invalid format)
5. Fill in the Phone field with "+1 (555) 111-2222"
6. Fill in the Company field with "Test Company"
7. Fill in the Position field with "Tester"
8. Click "Create" button

**Expected Results**:
- Validation error message appears for email field
- Error message indicates invalid email format
- Contact is not created
- Dialog remains open with data preserved

### Test Case 3.7: Create Contact with Special Characters
**Objective**: Test handling of special characters in contact fields

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in the Name field with "O'Brien-Smith"
4. Fill in the Email field with "test+user@company.co.uk"
5. Fill in the Phone field with "+44 (0) 20-1234-5678"
6. Fill in the Company field with "Smith & Jones LLC"
7. Fill in the Position field with "VP of R&D"
8. Click "Create" button

**Expected Results**:
- Contact is created successfully
- All special characters are preserved correctly
- Data is displayed correctly in the table

### Test Case 3.8: Create Contact with Very Long Names
**Objective**: Test field length limits and text overflow handling

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in the Name field with a very long string (60+ characters)
4. Fill in other fields with very long strings
5. Click "Create" button

**Expected Results**:
- If field length limits exist: validation error appears
- If no limits: contact is created and text is properly truncated or wrapped in table
- No UI breaking or layout issues occur

### Test Case 3.9: Create Duplicate Contact
**Objective**: Test system behavior when creating a contact with duplicate information

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click on "Add Contact" button
3. Fill in the Name field with "John Smith"
4. Fill in the Email field with "john.smith@example.com"
5. Fill in the Phone field with "+1 (555) 123-4567"
6. Fill in the Company field with "Acme Corporation"
7. Fill in the Position field with "Sales Manager"
8. Click "Create" button

**Expected Results**:
- If duplicates are prevented: error message appears
- If duplicates are allowed: contact is created (warning may appear)
- System behavior is consistent and predictable

---

## Test Suite 4: View Contact Details

### Test Case 4.1: Open Contact Detail Page
**Objective**: Verify that clicking the View button opens the contact detail page

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Locate the contact "John Smith" in the table
3. Click the first action button (View icon - typically an eye icon)
4. Wait for the detail page to load

**Expected Results**:
- URL changes to https://v0-erp-application-development-eight.vercel.app/contacts/[contact-id]
- Contact detail page displays with "John Smith" as the heading
- "Back to Contacts" button is visible at the top
- Contact information is displayed in card format:
  - Email: john.smith@example.com (with email icon)
  - Phone: +1 (555) 123-4567 (with phone icon)
  - Company: Acme Corporation (with building icon)
  - Position: Sales Manager (with briefcase icon)
- "Orders" section is displayed
- Order count shows "0"
- Message "No orders found for this contact." is displayed

### Test Case 4.2: Navigate Back from Contact Detail Page
**Objective**: Verify the Back to Contacts button functionality

**Steps**:
1. Navigate to a contact detail page (John Smith's page)
2. Click "Back to Contacts" button
3. Wait for page to load

**Expected Results**:
- Returns to the contacts list page
- URL changes back to /contacts
- All contacts are still displayed in the table
- Previously viewed contact is still present in the list

### Test Case 4.3: Verify Contact Detail Layout
**Objective**: Ensure all contact information is properly displayed

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click View button for "John Smith"
3. Take a snapshot of the detail page

**Expected Results**:
- Page layout is clean and organized
- All fields have appropriate icons
- Text is readable and not overlapping
- Related orders section is clearly separated
- No console errors are present

---

## Test Suite 5: Edit Contact

### Test Case 5.1: Open Edit Contact Dialog
**Objective**: Verify that the Edit dialog opens with pre-populated data

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Locate the contact "John Smith" in the table
3. Click the second action button (Edit icon - typically a pencil icon)
4. Wait for the dialog to appear

**Expected Results**:
- Dialog with title "Edit Contact" appears
- Subtitle "Update the contact information below." is displayed
- Form is pre-populated with existing data:
  - Name: "John Smith"
  - Email: "john.smith@example.com"
  - Phone: "+1 (555) 123-4567"
  - Company: "Acme Corporation"
  - Position: "Sales Manager"
- "Cancel" button is present
- "Update" button is present
- Close button (X) is visible

### Test Case 5.2: Update Contact with Valid Changes
**Objective**: Successfully update a contact's information

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click the Edit button for "John Smith"
3. Clear the Phone field and type "+1 (555) 999-8888"
4. Clear the Position field and type "Senior Sales Manager"
5. Leave other fields unchanged
6. Click "Update" button
7. Wait for dialog to close

**Expected Results**:
- Dialog closes successfully
- Contact information is updated in the table
- Phone number shows "+1 (555) 999-8888"
- Position shows "Senior Sales Manager"
- Other fields remain unchanged
- Success message may appear (if implemented)

### Test Case 5.3: Cancel Contact Edit
**Objective**: Verify that canceling edit discards changes

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click the Edit button for "John Smith"
3. Clear the Phone field and type "+1 (555) 000-0000"
4. Click "Cancel" button
5. Verify the contact information in the table

**Expected Results**:
- Dialog closes
- Contact information remains unchanged
- Phone number is still the original value
- No data is saved

### Test Case 5.4: Update Contact with Empty Fields
**Objective**: Test validation when clearing required fields

**Steps**:
1. Navigate to https://v0-erp-application-development-eight.vercel.app/contacts
2. Click the Edit button for "John