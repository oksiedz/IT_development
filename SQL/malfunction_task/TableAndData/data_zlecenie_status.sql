SET IDENTITY_INSERT [dbo].[zlecenie_status] ON 

INSERT [dbo].[zlecenie_status] ([id], [kod], [opis]) VALUES (1, 1, N'zlecenie rozpoczete')
INSERT [dbo].[zlecenie_status] ([id], [kod], [opis]) VALUES (2, 2, N'awaria urządzenia')
INSERT [dbo].[zlecenie_status] ([id], [kod], [opis]) VALUES (3, 3, N'brak surowca')
INSERT [dbo].[zlecenie_status] ([id], [kod], [opis]) VALUES (4, 4, N'zlecenie wznowione')
INSERT [dbo].[zlecenie_status] ([id], [kod], [opis]) VALUES (5, 5, N'zlecenie zakonczone')
SET IDENTITY_INSERT [dbo].[zlecenie_status] OFF
GO