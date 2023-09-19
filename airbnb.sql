CREATE TABLE IF NOT EXISTS "users" (
  user_id SERIAL PRIMARY KEY,
  user_type VARCHAR NOT NULL,
  username VARCHAR NOT NULL,
  email VARCHAR NOT NULL,
  password VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS "room" (
  room_id SERIAL PRIMARY KEY,
  host_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
  room_name VARCHAR NOT NULL,
  description TEXT,
  capacity INT NOT NULL,
  price_per_night INT NOT NULL,
  has_ac BOOLEAN,
  has_toiletries BOOLEAN,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS "reservation" (
  reservation_id SERIAL PRIMARY KEY,
  guest_id INT NOT NULL REFERENCES users(user_id) ON DELETE CASCADE,
  room_id INT NOT NULL REFERENCES room(room_id) ON DELETE CASCADE,
  check_in_date TIMESTAMP NOT NULL,
  check_out_date TIMESTAMP NOT NULL,
  reservation_date TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS "reviews" (
  review_id SERIAL PRIMARY KEY,
  rating INTEGER,
  comment TEXT,
  review_date TIMESTAMP NOT NULL,
  reservation_id INT NOT NULL REFERENCES reservation(reservation_id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS "payment" (
  payment_id SERIAL PRIMARY KEY,
  payment_date TIMESTAMP NOT NULL,
  amount INT NOT NULL,
  reservation_id INT NOT NULL REFERENCES reservation(reservation_id) ON DELETE CASCADE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);


INSERT INTO users (user_type, username, email, password)
VALUES
  ('guest', 'user1', 'user1@example.com', 'password1'),
  ('host', 'host1', 'user2@example.com', 'password2'),
  ('host', 'host2', 'host1@example.com', 'password3');


INSERT INTO room (host_id, room_name, description, capacity, price_per_night, has_ac, has_toiletries)
VALUES
  (2, 'Room 101', 'Cozy room for two', 2, 50, true, false),
  (2, 'Room 102', 'Spacious suite', 4, 100, true, true),
  (3, 'Room 201', 'Single room with a view', 1, 75, false, true);


INSERT INTO reservation (guest_id, room_id, check_in_date, check_out_date, reservation_date)
VALUES
  (1, 1, '2023-10-01', '2023-10-05', '2023-09-15'),
  (1, 2, '2023-09-20', '2023-09-25', '2023-09-15'),
  (1, 3, '2023-11-01', '2023-11-05', '2023-09-15');

INSERT INTO payment (payment_date, amount, reservation_id)
VALUES
  ('2023-09-15', 100, 1),
  ('2023-09-16', 75, 2),
  ('2023-09-17', 50, 3);

INSERT INTO reviews (rating, comment, review_date, reservation_id)
VALUES
  (4, 'Great stay!', '2023-09-16', 1),
  (5, 'Excellent experience', '2023-09-18', 2),
  (3, 'Average room', '2023-09-20', 3);


-- Find a user who had the biggest amount of reservations
SELECT users.user_id, users.username
FROM users
WHERE users.user_id = (
  SELECT subquery.guest_id
  FROM (
    SELECT reservation.guest_id, COUNT(*) AS reservation_count
    FROM reservation
    GROUP BY reservation.guest_id
    ORDER BY reservation_count DESC
    LIMIT 1
  ) AS subquery
);

-- Find a host who earned the biggest amount of money for the last month
SELECT u.user_id, u.username AS hostname
FROM "users" u
WHERE u.user_id = (
  SELECT subquery.host_id
  FROM (
    SELECT r.host_id, SUM(p.amount) AS earnings
    FROM "room" r
    JOIN "reservation" rv ON r.room_id = rv.room_id
    JOIN "payment" p ON rv.reservation_id = p.reservation_id
    WHERE p.payment_date >= DATE_TRUNC('month', NOW()) - INTERVAL '1 month'
    GROUP BY r.host_id
    ORDER BY SUM(p.amount) DESC
    LIMIT 1
  ) AS subquery
);


-- Find a host with the best average rating
SELECT u.user_id, u.username AS hostname
FROM users u
WHERE u.user_id = (
  SELECT subquery.host_id
  FROM (
    SELECT r.host_id, AVG(reviews.rating) AS average_rating
    FROM room r
    JOIN reservation rv ON r.room_id = rv.room_id
    JOIN reviews ON rv.reservation_id = reviews.reservation_id
    GROUP BY r.host_id
    ORDER BY average_rating DESC
    LIMIT 1
  ) AS subquery
);
