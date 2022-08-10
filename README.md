<div align="center">

# Time and Attendance
The Time and Attendance System is a system that will assist the Human Resource
Office of a hospital by making shift and scheduling, time and attendance, and leave
application more convenient and simpler for both human resource personnel and
employees.

<br>

# Technology Stack Used
**- FastAPI**<br>
**- SQLAlchemy (ORM)**<br>
**- MySQL**<br>
**- jQuery**<br>
**- Bootstrap**<br>
**- Jinja2**<br>
**- InstaScan (QR Code Scanner)**<br>
**- Javascript (QR Code)**<br>

</div>

<br><br>

<div align='center'>


</div>



## Installation
- Clone the repository
<pre class="notranslate"><code>git clone https://github.com/jrglomar/time_and_attendance
</code></pre>

- Switch to the repo folder
<pre class="notranslate"><code>time_and_attendance
</code></pre>

- Create virtual environment
<pre class="notranslate"><code>python -m venv venv
</code></pre>

- Activate virtual environment (if error occur check this - https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows)
<pre class="notranslate"><code>venv\scripts\activate
</code></pre>

Install Dependencies
<pre class="notranslate"><code>pip install -r requirements.txt
</code></pre>

Run the database migrations (Set the database connection in database.py before migrating)  
<pre class="notranslate"><code>alembic upgrade head
</code></pre>

Start the local development server
<pre class="notranslate"><code>uvicorn main:app --reload
</code></pre>

## Login at APP_URL/time_and_attendance/login to browse the system
<div>
    <table>
        <thead>
            <tr>
                <th><strong>Email</strong></th>
                <th><strong>Password</strong></th>
                <th><strong>Role</strong></th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>admin@homies.com</td>
                <td>User01</td>
                <td>Admin</td>
            </tr>
            <tr>
                <td>hr@homies.com</td>
                <td>User01</td>
                <td>HR</td>
            </tr>
            <tr>
                <td>employee@homies.com</td>
                <td>User01</td>
                <td>Employee</td>
            </tr>
            <tr>
                <td>employee2@homies.com</td>
                <td>User01</td>
                <td>Employee</td>
            </tr>
            <tr>
                <td>employee3@homies.com</td>
                <td>User01</td>
                <td>Employee</td>
            </tr>
            <tr>
                <td>employee4@homies.com</td>
                <td>User01</td>
                <td>Employee</td>
            </tr>
        </tbody>
    </table>
</div>


