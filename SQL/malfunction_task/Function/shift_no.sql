/****** Object:  UserDefinedFunction [dbo].[shift_no]    Script Date: 17.12.2022 15:41:50 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[shift_no]
(
	-- Add the parameters for the function here
	@datetime datetime
)
RETURNS int
AS
BEGIN
	
	DECLARE @shift_no int
	SET @shift_no = CASE WHEN datepart(hour, @datetime) < 6 THEN 3
	                     WHEN datepart(hour, @datetime) < 14 tHEN 1
						 ELSE 2
						 END

	RETURN @shift_no

END
GO