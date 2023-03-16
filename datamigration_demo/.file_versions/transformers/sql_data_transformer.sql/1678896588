-- Docs: https://docs.mage.ai/guides/sql-blocks
SELECT blogs.userId, blogs.id, userdtls.firstname, userdtls.lastname, userdtls.email, blogs.title
FROM {{ df_2 }} blogs 
inner join {{ df_1 }} userdtls 
on userdetls.id = blogs.userId