-- Enable readable output format
.mode columns
.headers on

-- Instructions for students:
-- 1. Open SQLite in terminal: sqlite3 library.db
-- 2. Load this script: .read code.sql
-- 3. Exit SQLite: .exit


-- write your sql code here
SELECT Books.title, Members.name, Loans.loan_date FROM Books 
JOIN Loans ON Books.id=Loans.book_id 
JOIN Members ON Loans.member_id=Members.id;

SELECT Books.title, Loans.loan_date FROM Books 
LEFT JOIN Loans ON Books.id=Loans.book_id;

SELECT Books.title, LibraryBranch.name FROM Books 
RIGHT JOIN LibraryBranch ON Books.branch_id=LibraryBranch.id;

SELECT LibraryBranch.name, COUNT(Books.id) AS BookCount FROM Books 
RIGHT JOIN LibraryBranch ON Books.branch_id=LibraryBranch.id
GROUP BY LibraryBranch.name;

SELECT LibraryBranch.name, COUNT(Books.id) AS BookCount FROM Books 
RIGHT JOIN LibraryBranch ON Books.branch_id=LibraryBranch.id
GROUP BY LibraryBranch.name HAVING BookCount>7;

SELECT Members.name, COUNT(Loans.id) AS LoanCount FROM Members
LEFT JOIN Loans ON Members.id=Loans.member_id
GROUP BY Members.name;

SELECT Members.name, COUNT(Loans.id) AS LoanCount FROM Members
LEFT JOIN Loans ON Members.id=Loans.member_id
GROUP BY Members.name HAVING LoanCount=0;

SELECT LibraryBranch.name, COUNT(Loans.id) AS LoanCount FROM LibraryBranch 
LEFT JOIN Books ON LibraryBranch.id=Books.branch_id
LEFT JOIN Loans ON Books.id=Loans.book_id
GROUP BY LibraryBranch.name;

SELECT Members.name AS LoanCount FROM Members
JOIN Loans ON Members.id=Loans.member_id
GROUP BY Members.name HAVING COUNT(Loans.return_date)<COUNT(Loans.loan_date);

SELECT Books.title,
CASE
    WHEN COUNT(Loans.return_date)<COUNT(Loans.loan_date) THEN
    'Unloaned book.'
    ELSE 'Loaned book.'
END AS loanStatus
FROM Books 
LEFT JOIN Loans ON Books.id=Loans.book_id
GROUP BY Books.title;