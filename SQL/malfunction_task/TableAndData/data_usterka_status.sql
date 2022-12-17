SET IDENTITY_INSERT [dbo].[usterka_status] ON 

INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (1, 0, N'urządzenie działa poprawnie')
INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (2, 1, N'przekazanie informacji do centrali')
INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (3, 2, N'diagnoza przyczyny awarii')
INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (4, 3, N'rozpoczęcie naprawy')
INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (5, 4, N'testy')
INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (6, 5, N'przywrócenie do etapu działania produkcyjnego')
INSERT [dbo].[usterka_status] ([id], [kod], [opis]) VALUES (7, 6, N'urządzenia nie udaje się naprawić podlega kasacji')
SET IDENTITY_INSERT [dbo].[usterka_status] OFF
GO